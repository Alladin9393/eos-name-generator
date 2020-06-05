"""
Provide tests for command line interface's generate name command.
"""
from click.testing import CliRunner
from cli.entrypoint import cli

from cli.constants import (
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from eos_name_generator.constants import EOS_NAME_LENGTH


def test_get_account_balance():
    """
    Case: generate random eos name.
    Expect: eos name is returned.
    """
    runner = CliRunner()
    result_name = runner.invoke(cli, [
        'generate',
        'name'
    ])

    assert PASSED_EXIT_FROM_COMMAND_CODE == result_name.exit_code
    assert isinstance(result_name, str)
    assert len(result_name) == EOS_NAME_LENGTH
