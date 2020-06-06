"""
Provide implementation of the command line interface to interact with `eos-name-generator`.
"""
import click

from cli.generate.cli import generate_commands


@click.group()
@click.version_option()
@click.help_option()
def cli():
    """
    Command-line interface to interact with `eos-name-generator`.
    """


cli.add_command(generate_commands)
