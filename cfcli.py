#!/usr/bin/env python3
import click
import lib
import sys
import subprocess
#from ddb_items import add_batch
#from ddb_items import add_item

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
    elif file:
        with open(file) as fin:
            read_data = fin.read()
        ret = "add_batch(file)"
        click.echo(f"Processing batch @ {file}. \n--> adding: \n{read_data}")
    elif name:
        ret = "add_batch(file)"
        click.echo('\n'.join(name))


'''
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
'''

if __name__ == "__main__":
    cli()
