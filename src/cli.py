import click
from loguru import logger


@click.group()
def cli() -> None:
    """Command Line Interface group."""


@cli.command()
def test() -> None:
    """Test command."""
    logger.info("Hi, there!")
