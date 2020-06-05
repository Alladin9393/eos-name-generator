"""
Provide implementation of the command line interface's generate commands.
"""
import click

from eos_name_generator import RandomNameGenerator
from cli.utils import (
    print_errors,
    print_result,
)


@click.group('generate', chain=True)
def generate_commands():
    """
    Provide commands for working with generation name.
    """


@generate_commands.command('name')
def generate_name():
    """
    Generate random name.
    """
    generator = RandomNameGenerator()

    random_name = ''
    try:
        random_name = generator.generate()

    except Exception as error:
        print_errors(str(error))

    print_result(random_name)


@click.option('--num', type=int, required=True)
@generate_commands.command('names_list')
def names_list(num):
    """
    Generate random list of names.
    """
    generator = RandomNameGenerator()

    random_name = ''
    try:
        random_name = generator.generate_list(num=num)

    except Exception as error:
        print_errors(str(error))

    random_name_str = '\n'
    random_name_str = random_name_str.join(random_name)

    print_result(random_name_str)
