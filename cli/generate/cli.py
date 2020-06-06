"""
Provide implementation of the command line interface's generate commands.
"""
import sys

import click

from cli.constants import (
    FAILED_EXIT_FROM_COMMAND_CODE,
    FAST_RANDOM_CHOICE_PROVIDER,
    NUMBERS_PROBABILITY,
    NUMPY_RANDOM_PROVIDER,
)
from cli.generate.forms import GenerateNameForm
from cli.generate.help import (
    NUM_HELP_MESSAGE,
    NUMBERS_PROBABILITY_HELP_MESSAGE,
    NUMPY_RANDOM_PROVIDER_HELP_MESSAGE,
    SEED_DATA_PATH_HELP_MESSAGE,
)
from cli.utils import (
    print_errors,
    print_result,
)
from eos_name_generator import RandomNameGenerator
from eos_name_generator.constants import SEED_DATA_PATH


@click.group('generate', chain=True)
def generate_commands():
    """
    Provide commands for working with generation name.
    """


@click.option('--numpy-random-provider', is_flag=True, required=False, help=NUMPY_RANDOM_PROVIDER_HELP_MESSAGE)
@click.option('--numbers-probabilities', type=float, required=False, help=NUMBERS_PROBABILITY_HELP_MESSAGE,
              default=NUMBERS_PROBABILITY)
@click.option('--seed-data-path', type=str, required=False, help=SEED_DATA_PATH_HELP_MESSAGE, default=SEED_DATA_PATH)
@generate_commands.command('name')
def generate_name(numpy_random_provider, numbers_probabilities, seed_data_path):
    """
    Generate random name.
    """
    arguments, errors = GenerateNameForm().load({
        'numpy_random_provider': numpy_random_provider,
        'numbers_probabilities': numbers_probabilities,
        'seed_data_path': seed_data_path,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    numpy_random_provider = arguments.get('numpy_random_provider')
    numbers_probabilities = arguments.get('numbers_probabilities')
    seed_data_path = arguments.get('seed_data_path')

    random_provider = FAST_RANDOM_CHOICE_PROVIDER
    if numpy_random_provider:
        random_provider = NUMPY_RANDOM_PROVIDER

    try:
        generator = RandomNameGenerator(
            random_provider_instance=random_provider,
            numbers_probabilities=numbers_probabilities,
            seed_data_path=seed_data_path,
        )
        random_name = generator.generate()

    except Exception as error:
        print_errors(errors=str(error))
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    print_result(random_name)


@click.option('--num', '-n', type=int, required=True, help=NUM_HELP_MESSAGE)
@click.option('--numpy-random-provider', is_flag=True, required=False, help=NUMPY_RANDOM_PROVIDER_HELP_MESSAGE)
@click.option('--numbers-probabilities', type=float, required=False, help=NUMBERS_PROBABILITY_HELP_MESSAGE,
              default=NUMBERS_PROBABILITY)
@click.option('--seed-data-path', type=str, required=False, help=SEED_DATA_PATH_HELP_MESSAGE, default=SEED_DATA_PATH)
@generate_commands.command('names_list')
def names_list(num, numpy_random_provider, numbers_probabilities, seed_data_path):
    """
    Generate random list of names.
    """
    arguments, errors = GenerateNameForm().load({
        'num': num,
        'numpy_random_provider': numpy_random_provider,
        'numbers_probabilities': numbers_probabilities,
        'seed_data_path': seed_data_path,
    })

    if errors:
        print_errors(errors=errors)
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    num = arguments.get('num')
    numpy_random_provider = arguments.get('numpy_random_provider')
    numbers_probabilities = arguments.get('numbers_probabilities')
    seed_data_path = arguments.get('seed_data_path')

    random_provider = FAST_RANDOM_CHOICE_PROVIDER
    if numpy_random_provider:
        random_provider = NUMPY_RANDOM_PROVIDER

    try:
        generator = RandomNameGenerator(
            random_provider_instance=random_provider,
            numbers_probabilities=numbers_probabilities,
            seed_data_path=seed_data_path,
        )
        random_name = generator.generate_list(num=num)

    except Exception as error:
        print_errors(errors=str(error))
        sys.exit(FAILED_EXIT_FROM_COMMAND_CODE)

    random_name_str = '\n'
    random_name_str = random_name_str.join(random_name)

    print_result(random_name_str)
