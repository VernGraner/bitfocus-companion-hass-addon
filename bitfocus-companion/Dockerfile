ARG BUILD_ARCH=aarch64

# Selecteer de juiste image op basis van de architectuur linux/arm64=aarch64_image linux/amd64=amd64_image
FROM ghcr.io/bitfocus/companion/companion:5.0.6-9750-stable-1acd2318f5@sha256:4628a7b3187add121395c5748c388e024e71861d85bc570d9a6c95b96ab47234 AS aarch64_image
FROM ghcr.io/bitfocus/companion/companion:5.0.6-9750-stable-1acd2318f5@sha256:35c51b025ff0906d0b8ea8d861a35dbbef154df2e175f514e103540c14e17ca8 AS amd64_image

# De eigenlijke image die wordt gebruikt
FROM ${BUILD_ARCH}_image

USER root

# Kopieer het startup script
COPY run.sh /run_companion.sh
RUN sed -i 's/\r$//' /run_companion.sh && chmod +x /run_companion.sh

# Verander het entrypoint
ENTRYPOINT ["/run_companion.sh"]
