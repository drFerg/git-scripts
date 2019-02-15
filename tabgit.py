#!/usr/bin/env python

""" A simple git tool for managing git repos based on tab's trello workflow

	tabgit branch BRANCH_TYPE URL - generate a branch name based on the BRANCH_TYPE and trello url
	tabgit fork BRANCH - generate a branch name fork incrementing the version of the specified BRANCH
	
	Add it to your bin to access anywhere
	ln -s ~/Projects/tabgit/tabgit.py /usr/local/bin/tabgit
"""

import click

@click.group()
def cli():
	pass

@cli.command()
@click.argument("branch_type")
@click.argument("url")
def branch(branch_type, url):
	card = url.split('/')[-1]
	card_words = url.split('/')[-1].split('-')
	card_id = card_words[0]
	card_name = "-".join(card_words[1:])

	branch_fmt = "{branch_type}/{id}/{version}/{desc}"

	branch_name = branch_fmt.format(branch_type=branch_type, id=card_id, version=1, desc=card_name)

	click.echo(branch_name)

@cli.command()
@click.argument("branch")
def fork(branch):
	parts = branch.split('/')
	parts[2] = str(int(parts[2]) + 1)
	forked = '/'.join(parts)
	click.echo(forked)


if __name__ == "__main__":
	cli()