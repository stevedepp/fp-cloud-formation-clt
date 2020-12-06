#!/usr/bin/env python3
import click
import lib
import sys
import subprocess

from ddb_ops import table_timestamp, item_add, items_add, items_delete, item_update, items_list

@click.version_option(lib.__version__)
@click.group()
def cli():
    '''greetings'''

@cli.command("make-infra")
def hello():
    # change to make infra and save/publish time
    subprocess.run(['make', 'infra'])

@cli.command("add")
@click.option('--file', '-f', help='File containig a column of names')
@click.option('--item', '-i', multiple=True, help='One item via --item or several separated by -i')
def add(file, item):
    if not file and not item:
        click.echo("--file or --items is required")
    elif file and item:
        click.echo("--file or --items but not both please")
    else:
        items_list_before = items_list()
        click.echo(f"Current items in DynamoDB are: {items_list_before}")
        if file:
            with open(file) as fin:
                list_to_add = fin.read().splitlines()
        elif item:
            list_to_add = list(item)
            file = 'list'
        click.echo(f"Adding these items from {file} to DynamoDB: {list_to_add}")
        items_add(list_to_add)
        items_list_after = items_list()
        items_added = list(set(items_list_after) - set(items_list_before))
        click.echo(f"Net, processing batch from {file}. \n-> adding: {items_added}")
        click.echo(f"full list will be {items_list_after}")

@cli.command("remove")
@click.option('--file', '-f', help='File containig a column of names')
@click.option('--item', '-i', multiple=True, help='One item via --item or several separated by -i')
def delete(file, item):
    if not file and not item:
        click.echo("--file or --item is required")
    elif file and item:
        click.echo("--file or --item but not both please")
    else:
        items_list_before = items_list()
        click.echo(f"Current items in DynamoDB are: {items_list_before}")
        if file:
            with open(file) as fin:
                list_to_delete = fin.read().splitlines()
        elif item:
            list_to_delete = list(item)
            file = 'list'
        click.echo(f"Deleting these items from {file} from DynamoDB: {list_to_delete}")
        items_delete(list_to_delete)
        items_list_after = items_list()
        items_deleted = list(set(items_list_before)-set(items_list_after))
        click.echo(f"Net, processing batch from {file}. \n-> deleting: {items_deleted}")
        click.echo(f"full list will be {items_list_after}")
        subprocess.run(['aws', 's3', 'rm', 's3://fangsentiment-depp', '--recursive'])

@cli.command("update")
@click.option('--old', '-o', help='Item that needs updating; use --old or -o')
@click.option('--new', '-n', help='Items new value; use --new or -n')
def update(old, new):
    if not old and not new:
        click.echo("--old AND --new is required")
    else:
        items_list_before = items_list()
        click.echo(f"Current items in DynamoDB are: {items_list_before}")
        click.echo(f"Update from {old} to {new}")
        item_update(old, new)
        items_list_after = items_list()
        click.echo(f"full list will be {items_list_after}")
        subprocess.run(['aws', 's3', 'rm', 's3://fangsentiment-depp', '--recursive'])

@cli.command("teardown")
def end():
    # change to make infra and save/publish time
    subprocess.run(['make','teardown'])

if __name__ == "__main__":
    cli()
