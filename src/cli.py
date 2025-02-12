import click
from loguru import logger


@click.group()
def cli():
    pass


@cli.command()
def tr() -> None:
    logger.info("hi, there")