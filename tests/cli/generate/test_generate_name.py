"""
Provide tests for command line interface's generate name command.
"""
from os.path import dirname

from click.testing import CliRunner

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    PASSED_EXIT_FROM_COMMAND_CODE,
)
from cli.entrypoint import cli
from cli.utils import dict_to_pretty_json
from eos_name_generator.constants import EOS_NAME_LENGTH


def test_generate_name():
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


def test_generate_name_with_numpy_provider():
    """
    Case: generate random eos name with `numpy.random` as random provider.
    Expect: eos name is returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'generate',
        'name',
        '--numpy-random-provider',
    ])
    random_name = result.output.splitlines()[0]

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(random_name, str)
    assert len(random_name) == EOS_NAME_LENGTH


def test_generate_name_with_numbers_probabilities():
    """
    Case: generate random eos name with `numbers probability`.
    Expect: eos name is returned.
    """
    numbers_probability = 0.5
    runner = CliRunner()
    result = runner.invoke(cli, [
        'generate',
        'name',
        '--numbers-probabilities',
        numbers_probability,
    ])
    random_name = result.output.splitlines()[0]

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(random_name, str)
    assert len(random_name) == EOS_NAME_LENGTH


def test_generate_name_with_custom_seed_data_path():
    """
    Case: generate random eos name with custom seed data path.
    Expect: eos name is returned.
    """
    data_path = dirname(__file__) + '/' + '../custom_data/data.txt'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'generate',
        'name',
        '--seed-data-path',
        data_path,
    ])
    random_name = result.output.splitlines()[0]

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert isinstance(random_name, str)
    assert len(random_name) == EOS_NAME_LENGTH


def test_generate_name_with_invalid_numbers_probabilities():
    """
    Case: generate random eos name with invalid `numbers probabilities`.
    Expect: eos name is returned.
    """
    invalid_numbers_probabilities = [-1, 2]
    runner = CliRunner()

    for invalid_numbers_probability in invalid_numbers_probabilities:
        result = runner.invoke(cli, [
            'generate',
            'name',
            '--numbers-probabilities',
            invalid_numbers_probability,
        ])

        expected_error = {
            "numbers_probabilities": [
                "Numbers probabilities must be between 0 and 1.",
            ],
        }

        assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
        assert dict_to_pretty_json(expected_error) in result.output


def test_generate_name_with_invalid_custom_seed_data():
    """
    Case: generate random eos name with invalid custom seed data.
    Expect: eos name is returned.
    """
    invalid_data = dirname(__file__) + '/' + '../custom_data/invalid_data.txt'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'generate',
        'name',
        '--seed-data-path',
        invalid_data,
    ])
    expected_error = 'Data contains invalid characters or does not match the name length error'

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_error in result.output


def test_generate_name_with_invalid_custom_seed_data_path():
    """
    Case: generate random eos name with invalid custom seed data path.
    Expect: eos name is returned.
    """
    invalid_data_path = dirname(__file__) + '/' + '../custom_data/data1.txt'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'generate',
        'name',
        '--seed-data-path',
        invalid_data_path,
    ])
    expected_error = f'[Errno 2] No such file or directory: \'{invalid_data_path}\''

    print(result.output)
    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_error in result.output
