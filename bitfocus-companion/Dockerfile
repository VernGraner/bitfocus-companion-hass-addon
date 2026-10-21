ARG BUILD_ARCH=aarch64

# Selecteer de juiste image op basis van de architectuur linux/arm64=aarch64_image linux/amd64=amd64_image
FROM ghcr.io/bitfocus/companion/companion:5.1.1-10000-stable-1e2454ae78@sha256:88d148297c00f90c3ab76fe66c65b1a2a38687a322553de2f8c530a4330c1fb0 AS aarch64_image
FROM ghcr.io/bitfocus/companion/companion:5.1.1-10000-stable-1e2454ae78@sha256:8e30cd1652b5aacaccaeb3913dd2a2406f1c7c8531713503caf1557843775614 AS amd64_image

# De eigenlijke image die wordt gebruikt
FROM ${BUILD_ARCH}_image

USER root

# Kopieer het startup script
COPY run.sh /run_companion.sh
RUN sed -i 's/\r$//' /run_companion.sh && chmod +x /run_companion.sh

# Verander het entrypoint
ENTRYPOINT ["/run_companion.sh"]
