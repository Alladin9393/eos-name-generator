"""
Provide tests for RandomNameGenerator.
"""
from os.path import dirname

import numpy
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
    number_of_test = 1_000_00
    accuracy = 0.01
    name_generator = RandomNameGenerator()
    generated_names = name_generator.generate_list(num=number_of_test)

    for name in generated_names:
        assert EOS_NAME_LENGTH == len(name)
        assert isinstance(name, str)

    generated_names_set = set(generated_names)
    error_range = len(generated_names) - len(generated_names_set)

    assert number_of_test * accuracy > error_range


def test_generate_with_custom_data():
    """
    Case: generate random name based on custom data.
    Except: name is returned.
    """
    custom_data_path = dirname(__file__) + '/custom_data/data.txt'
    name_generator = RandomNameGenerator(seed_data_path=custom_data_path)
    name = name_generator.generate()

    assert EOS_NAME_LENGTH == len(name)
    assert isinstance(name, str)


def test_generate_with_numpy_random_provider():
    """
    Case: generate random name with `numpy.random` as `random_provider`.
    Except: name is returned.
    """
    name_generator = RandomNameGenerator(random_provider_instance=numpy.random)
    name = name_generator.generate()

    assert EOS_NAME_LENGTH == len(name)
    assert isinstance(name, str)


def test_generate_with_custom_numbers_probabilities():
    """
    Case: generate random name based on custom name probabilities.
    Expect: name is returned.
    """
    numbers_probabilities_tests = [0, 0.01, 0.3, 0.999, 1]

    for numbers_probabilities in numbers_probabilities_tests:
        name_generator = RandomNameGenerator(numbers_probabilities=numbers_probabilities)
        name = name_generator.generate()

        assert EOS_NAME_LENGTH == len(name)
        assert isinstance(name, str)


def test_generate_list():
    """
    Case: generate random name list.
    Except: lit names are returned.
    """
    number_of_names = 100
    name_generator = RandomNameGenerator()
    names_list = name_generator.generate_list(num=number_of_names)

    assert number_of_names == len(names_list)

    for name in names_list:
        assert EOS_NAME_LENGTH == len(name)
        assert isinstance(name, str)


def test_generate_with_invalid_data():
    """
    Case: generate random name with invalid data.
    Expected: no such file or directory error message.
    """
    invalid_data_path = dirname(__file__) + '/' + 'custom_data/invalid_data.txt'

    with pytest.raises(ValidationDataError):
        RandomNameGenerator(seed_data_path=invalid_data_path)


def test_generate_with_invalid_random_provider():
    """
    Case: generate random name with invalid random provider.
    Expected: the interface `random_provider` does not contain choice method error message.
    """
    with pytest.raises(AttributeError):
        RandomNameGenerator(random_provider_instance=None)


def test_generate_with_invalid_data_provider():
    """
    Case: generate random name with invalid data provider.
    Expected: the interface `data_provider` does not contain `get_dictionary_by_word_len` method error message.
    """
    generator = RandomNameGenerator()

    with pytest.raises(AttributeError):
        generator.data_provider = None


def test_generate_with_invalid_numbers_probabilities():
    """
    Case: generate random name based on custom number probabilities.
    Expect: not valid number probabilities error message.
    """
    invalid_numbers_probabilities_tests = [-999, -1, -1.0, 1.01, 999]
    invalid_numbers_probabilities_str = '0'

    with pytest.raises(ValueError):
        for numbers_probabilities in invalid_numbers_probabilities_tests:
            RandomNameGenerator(numbers_probabilities=numbers_probabilities)

    with pytest.raises(TypeError):
        RandomNameGenerator(numbers_probabilities=invalid_numbers_probabilities_str)


def test_generate_with_non_existing_data_path():
    """
    Case: generate random name with non-existing data path.
    Expected: no such file or directory error message.
    """
    non_existing_data_path = 'custom_data/data.txt'

    with pytest.raises(FileNotFoundError):
        RandomNameGenerator(seed_data_path=non_existing_data_path)


def test_generate_with_non_existing_numbers_probabilities():
    """
    Case: generate random name with non-existing numbers_probabilities.
    Expected: not supported between instances of 'int' and 'NoneType' error message.
    """
    non_existing_numbers_probabilities = None

    with pytest.raises(TypeError):
        RandomNameGenerator(numbers_probabilities=non_existing_numbers_probabilities)
