"""
Provide tests for DataReader.
"""
from os.path import dirname

import pytest

from eos_name_generator.errors import ValidationDataError
from eos_name_generator.random_generator.data_reader import DataReader


def test_get_dictionary_by_word_len():
    """
    Case: get dictionary by word length.
    Expected: dictionary is returned.
    """
    custom_data_path = dirname(__file__) + '/custom_data/data.txt'
    data_reader = DataReader(data_path=custom_data_path)
    base_dict = data_reader.get_dictionary_by_word_len()

    assert len(base_dict) != 0


def test_get_dictionary_by_word_len_with_invalid_data():
    """
    Case: get dictionary by word len with invalid data.
    Expect: data contains invalid characters or does not match the name length error error message.
    """
    invalid_data_path = dirname(__file__) + '/custom_data/invalid_data.txt'
    data_reader = DataReader(data_path=invalid_data_path)

    with pytest.raises(ValidationDataError):
        data_reader.get_dictionary_by_word_len()


def test_get_dictionary_by_word_len_with_non_existing_data_path():
    """
    Case: test get dictionary by word len with non-existing data path.
    Expect: no such file or directory error message.
    """
    data_reader = DataReader(data_path='')
    with pytest.raises(FileNotFoundError):
        data_reader.get_dictionary_by_word_len()
