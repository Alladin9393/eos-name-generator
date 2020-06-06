"""
Provide tests for command line interface's generate names list command.
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

NUMBER_OF_GENERATED_NAMES = 1000


def test_generate_names_list():
    """
    Case: generate random eos list of names.
    Expect: eos names are returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'generate',
        'names_list',
        '--num',
        NUMBER_OF_GENERATED_NAMES
    ])
    random_names = result.output.splitlines()

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    for name in random_names:
        assert isinstance(name, str)
        assert len(name) == EOS_NAME_LENGTH


def test_generate_names_list_with_numpy_provider():
    """
    Case: generate random eos list of names with `numpy.random` as random provider.
    Expect: eos names are returned.
    """
    runner = CliRunner()
    result = runner.invoke(cli, [
        'generate',
        'names_list',
        '--num',
        NUMBER_OF_GENERATED_NAMES,
        '--numpy-random-provider'
    ])
    random_names = result.output.splitlines()

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    for name in random_names:
        assert isinstance(name, str)
        assert len(name) == EOS_NAME_LENGTH


def test_generate_names_list_with_numbers_probabilities():
    """
    Case: generate random eos list of names with `numbers probability`.
    Expect: eos names are returned.
    """
    numbers_probability = 0.5
    runner = CliRunner()
    result = runner.invoke(cli, [
        'generate',
        'names_list',
        '--num',
        NUMBER_OF_GENERATED_NAMES,
        '--numbers-probabilities',
        numbers_probability,
    ])
    random_names = result.output.splitlines()

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    for name in random_names:
        assert isinstance(name, str)
        assert len(name) == EOS_NAME_LENGTH


def test_generate_names_list_with_custom_seed_data_path():
    """
    Case: generate random eos list of names with custom seed data path.
    Expect: eos names are returned.
    """
    data_path = dirname(__file__) + '/' + '../custom_data/data.txt'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'generate',
        'names_list',
        '--num',
        NUMBER_OF_GENERATED_NAMES,
        '--seed-data-path',
        data_path
    ])
    random_names = result.output.splitlines()

    assert PASSED_EXIT_FROM_COMMAND_CODE == result.exit_code
    for name in random_names:
        assert isinstance(name, str)
        assert len(name) == EOS_NAME_LENGTH


def test_generate_names_list_with_invalid_numbers_probabilities():
    """
    Case: generate random eos list of names with invalid `numbers probabilities`.
    Expect: eos names are returned.
    """
    invalid_numbers_probabilities = [-1, 2]
    runner = CliRunner()

    for invalid_numbers_probability in invalid_numbers_probabilities:
        result = runner.invoke(cli, [
            'generate',
            'names_list',
            '--num',
            NUMBER_OF_GENERATED_NAMES,
            '--numbers-probabilities',
            invalid_numbers_probability,
        ])

        expected_error = {
            "numbers_probabilities": [
                "Numbers probabilities must be between 0 and 1."
            ]
        }

        assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
        assert dict_to_pretty_json(expected_error) in result.output


def test_generate_names_list_with_invalid_custom_seed_data():
    """
    Case: generate random eos list of names with invalid custom seed data.
    Expect: eos names are returned.
    """
    invalid_data = dirname(__file__) + '/' + '../custom_data/invalid_data.txt'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'generate',
        'names_list',
        '--num',
        NUMBER_OF_GENERATED_NAMES,
        '--seed-data-path',
        invalid_data
    ])
    expected_error = 'Data contains invalid characters or does not match the name length error'

    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_error in result.output


def test_generate_names_list_with_invalid_custom_seed_data_path():
    """
    Case: generate random eos list of names with invalid custom seed data path.
    Expect: eos names are returned.
    """
    invalid_data_path = dirname(__file__) + '/' + '../custom_data/data1.txt'

    runner = CliRunner()
    result = runner.invoke(cli, [
        'generate',
        'names_list',
        '--num',
        NUMBER_OF_GENERATED_NAMES,
        '--seed-data-path',
        invalid_data_path
    ])
    expected_error = f'[Errno 2] No such file or directory: \'{invalid_data_path}\''

    print(result.output)
    assert FAILED_EXIT_FROM_COMMAND_CODE == result.exit_code
    assert expected_error in result.output
