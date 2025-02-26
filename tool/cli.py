#!/usr/bin/env python3

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
    logger.info("hi, there")
