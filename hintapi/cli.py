from __future__ import annotations

import click

from .__version__ import __version__
from .routing.commands import display_urls
from .utils import import_module


@click.group(help=f"HintAPI {__version__}")
def index_cli():
    pass


index_cli.add_command(display_urls, "display-urls")

import_module("commands")
