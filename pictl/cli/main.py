"""The PICTL module"""

import click
from rich import print as rprint

from pictl import __version__
from pictl.config import Config
from pictl.pic import compress as pcom
from pictl.upload import upload as pup

CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


def get_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f"PICTL {__version__}")
    ctx.exit()


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option(
    "-V",
    "--version",
    help="Show the pictl version.",
    callback=get_version,
    expose_value=False,
    is_eager=True,
    is_flag=True,
)
def cli():
    """A command line tool for image processing and uploading (ex. S3-type).

    \b
    Now it supports:
      - transformation from other image types to `webp` image as well as
        image compression.
      - image file uploading to AWS S3 or Cloudflare R2.
    """


@click.group()
def config():
    """Operations for the config file `~/.pictlrc`."""


@config.command()
def info():
    """Check the configs."""
    try:
        c = Config()
        settings = c.read()
        rprint(settings)
    except FileNotFoundError:
        rprint(f"{c.rc} doesn't exsit. Please check it.")


@config.command()
def add():
    """Add configs to the config file."""
    try:
        c = Config()
        c.read()
        c.add()
    except FileNotFoundError:
        c.init()
        c.add()


@config.command()
@click.option("-g", "--group", help="The specified group name.")
def delete(group: str = None):
    """Delete config group from the config file."""
    try:
        c = Config()
        c.read()
        c.delete(group)
    except FileNotFoundError:
        rprint(f"{c.rc} doesn't exsit. Please check it.")


@config.command()
def init():
    """Initialize config file with default configs."""
    Config().init()


@click.command()
@click.argument("filename")
@click.argument("group")
def cup(filename: str, group: str):
    """Compress image and upload to remote storage (compress and upload).

    \b
    FILENAME is the name of the file to compress.
    GROUP is the group in the config file you want to use.
    """
    output = pcom(filename)
    if output is not None:
        pup(output, group)


@click.command()
@click.argument("filename")
@click.option("-o", "--output", help="The output filename.")
def compress(filename, output: str = None):
    """Compress any image into `webp` image.

    FILENAME is the name of the file to compress.
    """
    pcom(filename, output)


@click.command()
@click.argument("filename")
@click.argument("group")
def upload(filename: str, group: str):
    """Upload the file to remote storage.

    \b
    FILENAME is the name of the file to upload.
    GROUP is the group in the config file you want to use.
    """
    pup(filename, group)


cli.add_command(config)
cli.add_command(upload)
cli.add_command(compress)
cli.add_command(cup)

if __name__ == "__main__":
    cli()
