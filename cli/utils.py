"""
Provide utils for command line interface.
"""
import click


def print_result(result):
    """
    Print successful result to the terminal.
    """
    return click.echo(result)


def print_errors(errors):
    """
    Print error messages to the terminal.

    Arguments:
        errors (string or dict): dictionary with error messages.
    References:
        - https://click.palletsprojects.com/en/7.x/utils/#ansi-colors
    """
    click.secho(errors, blink=True, bold=True, fg='red')
