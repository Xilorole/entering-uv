# entering uv

## Overview

This repository contains a Python project that leverages `uv` for package management and `click` for creating a command-line interface (CLI). The project aims to provide a streamlined and efficient development experience for Python developers.

## Features

- **CLI Tool**: A command-line interface built with `click`.
- **Logging**: Integrated logging using `loguru`.
- **Package Management**: Utilizes `uv` for fast and efficient package management.

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/entering-uv.git
    cd entering-uv
    ```

2. **Install `uv`**:
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

3. **Pin Python version and sync dependencies**:
    ```sh
    uv python pin "$(cat .python-version)"
    uv sync --dev
    ```

## Usage

### CLI Commands

The project includes a CLI tool with the following commands:

- **hello**: Logs a greeting message.

To use the CLI, run:
```sh
uv run tool hello
```

## Development

### Requirements

- Python 3.13
- `uv`
- `click`
- `loguru`

### Setting Up Development Environment

1. **Install dependencies**:
    ```sh
    uv sync --dev
    ```

2. **Run the CLI**:
    ```sh
    uv run tool hello
    ```

### Linting and Formatting

The project uses `ruff` for linting and formatting. To automatically fix issues, run:
```sh
uv run ruff --fix .
```

## Development Container

This project includes a development container configuration for Visual Studio Code.

### Features

- **Base Image**: `mcr.microsoft.com/vscode/devcontainers/base:bookworm`
- **Installed Tools**: `uv`, `gh`, `starship`, `hadolint`
- **VS Code Extensions**: Includes extensions for Python, Docker, Git, Markdown, and more.

### Setup

1. **Open the project in VS Code**.
2. **Reopen in Container**: When prompted, reopen the project in the development container.

### Post Create Command

After the container is created, the following command will run to set up the environment:
```sh
/bin/zsh .devcontainer/postCreateCommand.sh
```

This script will:
- Pin the Python version.
- Sync the development dependencies.
- Initialize the `starship` prompt.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
