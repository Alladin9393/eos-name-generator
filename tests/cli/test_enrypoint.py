"""
Provide tests for implementation of the entrypoint commands.
"""
from cli.entrypoint import cli


def test_name():
    """
    Case: get the name of the CLI entrypoint function.
    Expect: the name is the same as in setup.py (`cli`).
    """
    assert 'cli' == cli.name
