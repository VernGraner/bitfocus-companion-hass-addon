ARG BUILD_ARCH=aarch64

# Selecteer de juiste image op basis van de architectuur linux/arm64=aarch64_image linux/amd64=amd64_image
FROM ghcr.io/bitfocus/companion/companion:5.1.0-9981-stable-257b325d09@sha256:a30a74694230fb27c3be481552062a72820dffa76631ffba164f8de9262c36a0 AS aarch64_image
FROM ghcr.io/bitfocus/companion/companion:5.1.0-9981-stable-257b325d09@sha256:c348fcc7822bc68c83a95a2daf4918e13c502e9d9fda7ab2edd125f6fd1e6ad8 AS amd64_image

# De eigenlijke image die wordt gebruikt
FROM ${BUILD_ARCH}_image

USER root

# Kopieer het startup script
COPY run.sh /run_companion.sh
RUN sed -i 's/\r$//' /run_companion.sh && chmod +x /run_companion.sh

# Verander het entrypoint
ENTRYPOINT ["/run_companion.sh"]
