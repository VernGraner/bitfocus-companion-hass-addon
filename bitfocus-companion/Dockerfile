ARG BUILD_ARCH=aarch64

# Selecteer de juiste image op basis van de architectuur linux/arm64=aarch64_image linux/amd64=amd64_image
FROM ghcr.io/bitfocus/companion/companion:5.1.2-10019-stable-98d5d4e1a1@sha256:2139b2b66865f73f800fdc6b3b50cd55af53e6e7ca6c3a34e90c03d2220ceffa AS aarch64_image
FROM ghcr.io/bitfocus/companion/companion:5.1.2-10019-stable-98d5d4e1a1@sha256:726f20280d0414e58e8a98f7000f303baf2a81eede81485aafcfdf4782321ab1 AS amd64_image

# De eigenlijke image die wordt gebruikt
FROM ${BUILD_ARCH}_image

USER root

# Kopieer het startup script
COPY run.sh /run_companion.sh
RUN sed -i 's/\r$//' /run_companion.sh && chmod +x /run_companion.sh

# Verander het entrypoint
ENTRYPOINT ["/run_companion.sh"]
