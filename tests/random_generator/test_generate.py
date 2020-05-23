"""
Provide tests for command line interface's account get balance command.
"""
from os.path import dirname
import pytest

from eos_name_generator import RandomNameGenerator
from eos_name_generator.constants import EOS_NAME_LENGTH
from eos_name_generator.errors import ValidationDataError


def test_generate():
    """
    Case: generate random `EOS` name.
    Expect: name is returned.
    """
    name_generator = RandomNameGenerator()
    name = name_generator.generate()

    assert EOS_NAME_LENGTH == len(name)
    assert isinstance(name, str)


def test_sustainability_of_algorithm():
    """
    Case: generate batch of `EOS` names to test sustainability of the algorithm.
    Expect: name is returned.
    """
    number_of_test = 100_000
    name_generator = RandomNameGenerator()
    generated_names = []

    for _ in range(number_of_test):
        name = name_generator.generate()
        generated_names.append(name)

        assert EOS_NAME_LENGTH == len(name)
        assert isinstance(name, str)

    # remove comment when `generate` method logic will be complete
    # generated_names_set = set(generated_names)

    # assert len(generated_names) == len(generated_names_set)


def test_generate_with_custom_data():
    """
    Case: generate random name based on custom data.
    Except: name is returned.
    """
    custom_data_path = dirname(__file__) + '/custom_data/data.txt'
    name_generator = RandomNameGenerator(generation_base_data_path=custom_data_path)
    name = name_generator.generate()

    assert EOS_NAME_LENGTH == len(name)
    assert isinstance(name, str)


def test_generate_with_custom_numbers_probabilities():
    """
    Case: generate random name based on custom name probabilities.
    Expect: name is returned.
    """
    numbers_probabilities = 0.3
    name_generator = RandomNameGenerator(numbers_probabilities=numbers_probabilities)
    name = name_generator.generate()

    assert EOS_NAME_LENGTH == len(name)
    assert isinstance(name, str)


def test_generate_with_invalid_data():
    """
    Case: generate random name with invalid data.
    Expected: no such file or directory error message.
    """
    invalid_data_path = dirname(__file__) + '/' + 'custom_data/invalid_data.txt'

    with pytest.raises(ValidationDataError):
        RandomNameGenerator(generation_base_data_path=invalid_data_path)


def test_generate_with_invalid_number_probabilities():
    """
    Case: generate random name based on custom name probabilities.
    Expect: not valid number probabilities error message.
    """


def test_generate_with_non_existing_data_path():
    """
    Case: generate random name with non-existing data path.
    Expected: no such file or directory error message.
    """
    non_existing_data_path = 'custom_data/data.txt'

    with pytest.raises(FileNotFoundError):
        RandomNameGenerator(generation_base_data_path=non_existing_data_path)
