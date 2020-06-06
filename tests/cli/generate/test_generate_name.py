"""
Provide tests for command line interface's generate name command.
"""
from click.testing import CliRunner

from cli.constants import PASSED_EXIT_FROM_COMMAND_CODE
from cli.entrypoint import cli
from eos_name_generator.constants import EOS_NAME_LENGTH


def test_get_account_balance():
    """
    Case: generate random eos name.
    Expect: eos name is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'generate',
        'name',
    ])
    random_name = result.output.splitlines()[0]

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(random_name, str)
    assert len(random_name) == EOS_NAME_LENGTH
