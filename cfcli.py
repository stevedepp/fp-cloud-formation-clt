#!/usr/bin/env python3
import click
import lib
import sys
import subprocess
from ddb_new_items import add_batch

@click.version_option(lib.__version__)
@click.group()
def cli():
    '''blah blah'''

@cli.command("make_infra")
def hello():
    print('hello')
    subprocess.run(['make', 'env'])

@cli.command("names")
@click.option('--file', help='File containig a column of names')
@click.option('--name', '-n', multiple=True, help='One name or several separated by -n')
def hello(file, name):
    if not file and not name:
        click.echo("--file or --name is required")
    elif file and name:
        click.echo("--file or --name but not both please")
    elif file:
        with open(file) as fin:
            list_from_file = fin.read().splitlines()
        all_items, new_items = add_batch(list_from_file)
        click.echo(f"Processing batch from {file}. \n-> adding: {new_items}")
        click.echo(f"full list will be {all_items}")
    elif name:
        list_from_user = list(name)
        all_items, new_items = add_batch(list_from_user)
        click.echo(f"Processing batch from user. \n-> adding: {new_items}")
        click.echo(f"full list will be {all_items}")

if __name__ == "__main__":
    cli()
