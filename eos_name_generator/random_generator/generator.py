"""
Provide an implementation of the RandomNameGenerator interface.
"""
from collections import defaultdict

from eos_name_generator.constants import (
    EOS_NAME_LENGTH,
    RANDOM_NAME_GENERATOR_BASE_DATA_PATH,
    RANDOM_NAME_GENERATOR_NUMBERS_PROBABILITIES,
)
from eos_name_generator.errors import ValidationDataError
from eos_name_generator.interfaces import BaseGeneratorInterface


class RandomNameGenerator(BaseGeneratorInterface):
    """
    Implementation of the RandomNameGenerator.
    """

    def __init__(
            self,
            generation_base_data_path=RANDOM_NAME_GENERATOR_BASE_DATA_PATH,
            numbers_probabilities=RANDOM_NAME_GENERATOR_NUMBERS_PROBABILITIES,
    ):
        self.__generation_base_data_path = generation_base_data_path
        self.__numbers_probabilities = numbers_probabilities
        self.__base_dict = self.__get_base_dict()

    def generate(self) -> str:
        """
        Generate `EOS` name method.

        :return: `EOS` name str
        """
        mock_name = 'accountnum12'
        return mock_name

    def generate_list(self) -> list:
        """
        Generate list of `EOS` names method.

        :return: list of `EOS` names
        """
        return []

    def __get_base_dict(self) -> defaultdict:
        with open(self.__generation_base_data_path) as f:
            data = f.read().splitlines()

        self.__validate_data(data)
        data_dictionary_by_word_len = defaultdict(list)
        for word in data:
            word_len = len(word)
            data_dictionary_by_word_len[word_len].append(word)

        return data_dictionary_by_word_len

    @staticmethod
    def __validate_data(data: list):
        for word in data:
            is_valid_word_len = (len(word) <= EOS_NAME_LENGTH)
            is_valid_word = word.isalpha() and word.islower() and is_valid_word_len

            if not is_valid_word:
                raise ValidationDataError("Data contains invalid characters or does not match the name length error")

    def __repr__(self):
        """
        Debug `repr` method.

        :return: RandomNameGenerator object state
        """
        return f'<RandomNameGenerator({self.__generation_base_data_path}, {self.__numbers_probabilities})>'
