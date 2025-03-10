import sys

import click
from loguru import logger


@click.group()
def cli() -> None:
    """Command Line Interface (CLI) entry point for the tool.

    This function serves as the main entry point for the CLI of the tool.
    It is intended to handle user inputs and execute the appropriate
    commands based on those inputs.
    Currently, this function is a placeholder and does not perform any
    operations.
    """


@cli.command()
def hello() -> None:
    """Log a greeting message."""
    python_version = sys.version
    logger.info(f"You are using Python {python_version}")


if __name__ == "__main__":
    cli()
