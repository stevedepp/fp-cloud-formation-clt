#!/usr/bin/env python3
import click
import sys
from ddb_items import add_batch
from ddb_items import add_item

@click.version_option(nlib.__version__)
@click.group()
def cli():
    '''blah blah'''

@cli.command('')

@cli.command("names")
@click.option('--file', help='Column of names')
@click.option('--name', help='Individual name')
def names(file, name):
    if not file and not name:
        click.echo("--file or --name is required")
        sys.exit(1)
    elif file:
        ret = add_batch(file)
        click.echo(f"Processing batch {batch} --> adding {ret}")
    elif name:
        ret = add_item(name)
        click.echo(f"Processing item {item} --> adding {ret}")

if __name__ == "__main__":
    cli()
