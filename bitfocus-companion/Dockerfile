ARG BUILD_ARCH=aarch64

# Selecteer de juiste image op basis van de architectuur linux/arm64=aarch64_image linux/amd64=amd64_image
FROM ghcr.io/bitfocus/companion/companion:5.0.1-9649-stable-6acd549dd5@sha256:91f0b19829528b271bb4d8af26d2269a3b2a7fdd489fab289e545fbb414b4270 AS aarch64_image
FROM ghcr.io/bitfocus/companion/companion:5.0.1-9649-stable-6acd549dd5@sha256:1e269a26a7b9305a4c93e0ef477a21c1555c50671ddb126f4380a93cbd20cf91 AS amd64_image

# De eigenlijke image die wordt gebruikt
FROM ${BUILD_ARCH}_image

USER root

# Kopieer het startup script
COPY run.sh /run_companion.sh
RUN sed -i 's/\r$//' /run_companion.sh && chmod +x /run_companion.sh

# Verander het entrypoint
ENTRYPOINT ["/run_companion.sh"]
