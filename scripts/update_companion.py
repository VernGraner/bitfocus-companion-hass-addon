#!/usr/bin/env python3
"""Update the Home Assistant add-on to the latest stable Companion image."""

from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCKERFILE = ROOT / "bitfocus-companion" / "Dockerfile"
CONFIG = ROOT / "bitfocus-companion" / "config.yaml"
CHANGELOG = ROOT / "bitfocus-companion" / "CHANGELOG.md"
IMAGE = "ghcr.io/bitfocus/companion/companion"
REPOSITORY = "bitfocus/companion/companion"
ACCEPT_INDEX = "application/vnd.oci.image.index.v1+json"


def get_json(url: str, headers: dict[str, str] | None = None) -> tuple[object, object]:
    request = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.load(response), response.headers


def latest_release() -> str:
    payload, _ = get_json(
        "https://api.github.com/repos/bitfocus/companion/releases/latest",
        {"Accept": "application/vnd.github+json", "User-Agent": "companion-hass-addon-updater"},
    )
    tag = payload["tag_name"]
    return tag.removeprefix("v")


def registry_token() -> str:
    query = urllib.parse.urlencode(
        {"service": "ghcr.io", "scope": f"repository:{REPOSITORY}:pull"}
    )
    payload, _ = get_json(f"https://ghcr.io/token?{query}")
    return payload["token"]


def stable_image_tag(version: str, token: str) -> str:
    url = f"https://ghcr.io/v2/{REPOSITORY}/tags/list?n=1000"
    pattern = re.compile(rf"^{re.escape(version)}-(\d+)-stable-[0-9a-f]+$")
    matches: list[tuple[int, str]] = []

    while url:
        payload, headers = get_json(url, {"Authorization": f"Bearer {token}"})
        for tag in payload.get("tags") or []:
            match = pattern.fullmatch(tag)
            if match:
                matches.append((int(match.group(1)), tag))

        link = headers.get("Link", "")
        next_match = re.search(r'<([^>]+)>;\s*rel="next"', link)
        url = urllib.parse.urljoin(url, next_match.group(1)) if next_match else ""

    if not matches:
        raise RuntimeError(f"No stable GHCR image found for Companion {version}")
    return max(matches)[1]


def platform_digests(tag: str, token: str) -> dict[str, str]:
    url = f"https://ghcr.io/v2/{REPOSITORY}/manifests/{tag}"
    payload, _ = get_json(
        url,
        {"Authorization": f"Bearer {token}", "Accept": ACCEPT_INDEX},
    )
    digests = {
        manifest["platform"]["architecture"]: manifest["digest"]
        for manifest in payload["manifests"]
        if manifest.get("platform", {}).get("os") == "linux"
        and manifest.get("platform", {}).get("architecture") in {"amd64", "arm64"}
    }
    if set(digests) != {"amd64", "arm64"}:
        raise RuntimeError(f"Expected amd64 and arm64 manifests, found {sorted(digests)}")
    return digests


def bump_addon_version(text: str) -> tuple[str, str]:
    match = re.search(r'(?m)^version:\s*"(\d+)\.(\d+)\.(\d+)"\s*$', text)
    if not match:
        raise RuntimeError("Could not find a three-part add-on version in config.yaml")
    major, minor, patch = map(int, match.groups())
    new_version = f"{major}.{minor}.{patch + 1}"
    return text[: match.start()] + f'version: "{new_version}"' + text[match.end() :], new_version


def main() -> int:
    version = latest_release()
    docker_text = DOCKERFILE.read_text(encoding="utf-8")
    current_match = re.search(
        r"ghcr\.io/bitfocus/companion/companion:([0-9]+\.[0-9]+\.[0-9]+)-",
        docker_text,
    )
    if not current_match:
        raise RuntimeError("Could not determine the current Companion version")
    if current_match.group(1) == version:
        print(f"Companion {version} is already configured")
        return 0

    token = registry_token()
    image_tag = stable_image_tag(version, token)
    digests = platform_digests(image_tag, token)

    updated_docker = re.sub(
        rf"{re.escape(IMAGE)}:[^@\s]+@sha256:[0-9a-f]+(?= AS aarch64_image)",
        f"{IMAGE}:{image_tag}@{digests['arm64']}",
        docker_text,
    )
    updated_docker = re.sub(
        rf"{re.escape(IMAGE)}:[^@\s]+@sha256:[0-9a-f]+(?= AS amd64_image)",
        f"{IMAGE}:{image_tag}@{digests['amd64']}",
        updated_docker,
    )
    if updated_docker == docker_text:
        raise RuntimeError("Dockerfile image references were not updated")

    config_text = CONFIG.read_text(encoding="utf-8")
    updated_config, addon_version = bump_addon_version(config_text)
    changelog_text = CHANGELOG.read_text(encoding="utf-8")
    changelog_entry = (
        f"## {addon_version}\n\n"
        f"- Updated Bitfocus Companion to v{version}.\n\n"
    )

    DOCKERFILE.write_text(updated_docker, encoding="utf-8")
    CONFIG.write_text(updated_config, encoding="utf-8")
    CHANGELOG.write_text(changelog_entry + changelog_text, encoding="utf-8")
    print(f"Updated add-on {addon_version} to Companion {version} ({image_tag})")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"Updater failed: {error}", file=sys.stderr)
        raise SystemExit(1)
