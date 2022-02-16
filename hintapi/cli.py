from __future__ import annotations

import os
import logging

import click

from .__version__ import __version__
from .routing.commands import display_urls
from .utils import import_module, import_from_string, F


@click.group(help=f"HintAPI {__version__}")
def index_cli():
    pass


LOGGING_LEVELS = {
    "critical": logging.CRITICAL,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "info": logging.INFO,
    "debug": logging.DEBUG,
}


def _serve(application: str, bind: str, log_level: str) -> None:
    import waitress

    wsgi_app = import_from_string(application)

    if bind.startswith("unix:"):
        bind_config = {
            "unix_socket": bind[5:] | F(os.path.normpath) | F(os.path.abspath)
        }
    else:
        if ":" in bind:
            host, port = bind.split(":")
            bind_config = {"host": host, "port": int(port)}
        else:
            bind_config = {"host": bind, "port": 4190}

    logging.getLogger("waitress").setLevel(LOGGING_LEVELS[log_level])

    waitress.serve(wsgi_app, **bind_config)


@index_cli.command(help="Use waitress to serve hintapi application")
@click.option(
    "--bind",
    default="127.0.0.1:4190",
    show_default=True,
    help="A string of the form: HOST:PORT, unix:PATH.",
)
@click.option(
    "--log-level",
    type=click.Choice(["critical", "error", "warning", "info", "debug"]),
    default="info",
    show_default=True,
)
@click.option(
    "--autoreload/--no-autoreload",
    default=True,
    show_default=True,
    help="Reload the application on python module changes",
)
@click.argument("application")
def serve(autoreload: bool, application: str, bind: str, log_level: str) -> None:
    import hupper

    if autoreload:
        # start_reloader will only return in a monitored subprocess
        reloader = hupper.start_reloader(
            "hintapi.cli._serve",
            worker_kwargs={
                "application": application,
                "bind": bind,
                "log_level": log_level,
            },
        )
        # monitor an extra file
        reloader.watch_files([".env"])

    _serve(application, bind, log_level)


index_cli.add_command(display_urls, "display-urls")

import_module("commands")
