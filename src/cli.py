import click
from loguru import logger


@click.group()
def cli():
    pass


@cli.command()
def hello() -> None:
    logger.info("hi, there")
