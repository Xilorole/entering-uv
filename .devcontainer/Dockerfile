FROM mcr.microsoft.com/vscode/devcontainers/base:bookworm

# Install uv
USER vscode
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
