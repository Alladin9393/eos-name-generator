"""
Provide implementation of the DataReader.
"""
from collections import defaultdict

from eos_name_generator.constants import EOS_NAME_LENGTH
from eos_name_generator.errors import ValidationDataError


class DataReader:
    """
    Implementation of the DataReader.
    """

    def __init__(self, data_path):
        self.data_path = data_path

    def get_dictionary_by_word_len(self) -> defaultdict:
        """
        Read data from `seed_data_path`.

        Read data from `seed_data_path` and transform it into `dictionary` object
        where the key is the word length.
        """
        with open(self.data_path) as f:
            data = f.read().splitlines()

        self.__validate_data(data)
        data_dictionary_by_word_len = defaultdict(list)
        for word in data:
            word_len = len(word)
            data_dictionary_by_word_len[word_len].append(word)

        return data_dictionary_by_word_len

    @staticmethod
    def __validate_data(data: list):
        """
        Seed data validation to generate the correct `eos` name.

        :param data: data to be validated
        """
        for word in data:
            is_valid_word_len = (len(word) <= EOS_NAME_LENGTH)
            is_valid_word = word.isalpha() and word.islower() and is_valid_word_len

            if not is_valid_word:
                raise ValidationDataError("Data contains invalid characters or does not match the name length error")
