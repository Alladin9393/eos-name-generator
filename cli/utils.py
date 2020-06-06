"""
Provide utils for command line interface.
"""
import json

import click


def dict_to_pretty_json(data):
    r"""
    Convert dictionary to json with indents (human readable string).

    From the following code:
        {
            "address": [
                "The following address `1120076ecf036e857f42129b5830` is invalid."
            ]
        }
    It creates:
        "{\n    \"address\": [\n        \"The following address `1120076ecf036e857f42129b5830` is invalid.\"    ]\n}\n"
    Notes:
        - `r` symbol at the start of the documentation is presented because of PEP257.
    References:
        - https://www.python.org/dev/peps/pep-0257/#id15
        - https://stackoverflow.com/a/33734332/9632462
    """
    return json.dumps(data, indent=4, sort_keys=True)


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
    click.secho(dict_to_pretty_json(errors), blink=True, bold=True, fg='red')
