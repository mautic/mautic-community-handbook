FROM python:3.11

# Keep version in sync with .github/workflows/linting.yml
ENV VALE_VERSION=3.7.1

WORKDIR /workspace

# Install required dependencies for reStructuredText validation
RUN pip install --no-cache-dir rst2html rstcheck

# Install Vale for linting
RUN mkdir -p /workspace/vale && cd /workspace/vale && \
    wget https://github.com/errata-ai/vale/releases/download/v${VALE_VERSION}/vale_${VALE_VERSION}_Linux_64-bit.tar.gz && \
    tar -xf vale_${VALE_VERSION}_Linux_64-bit.tar.gz && \
    mv /workspace/vale/vale /usr/local/bin/vale && \
    rm -rf /workspace/vale

# Add Python binaries to PATH
ENV PATH="/home/codespace/.local/bin:$PATH"

# Set up a non-root user (Codespaces uses 'codespace' instead of 'gitpod')
RUN useradd -l -u 1000 -G sudo -md /home/codespace -s /bin/bash -p codespace codespace

USER codespace
