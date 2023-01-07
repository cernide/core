#!/usr/bin/python
#
# Copyright 2018-2023 Polyaxon, Inc.
# This file and its contents are licensed under the AGPLv3 License.
# Please see the included NOTICE for copyright information and
# LICENSE-AGPL for a copy of the license.

import click


@click.command()
@click.option(
    "--host",
    help="The service host.",
)
@click.option(
    "--port",
    type=int,
    help="The service port.",
)
@click.option(
    "--workers",
    type=int,
    help="Number of workers.",
)
@click.option(
    "--per-core",
    is_flag=True,
    default=False,
    help="To enable workers per core.",
)
@click.option(
    "--uds",
    help="UNIX domain socket binding.",
)
def server(host: str, port: int, workers: int, per_core: bool, uds: str):
    """Start a new sandbox session."""
    from haupt.cli.runners.server import start

    return start(
        host=host,
        port=port,
        workers=workers,
        per_core=per_core,
        uds=uds,
    )
