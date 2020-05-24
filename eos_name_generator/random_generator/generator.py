"""
Provide an implementation of the RandomNameGenerator interface.
"""
from collections import defaultdict

from eos_name_generator.constants import (
    EOS_NAME_LENGTH,
    SEED_DATA_PATH,
    NUMBERS_PROBABILITIES,
)
from eos_name_generator.errors import ValidationDataError
from eos_name_generator.interfaces import BaseGeneratorInterface


class RandomNameGenerator(BaseGeneratorInterface):
    """
    Implementation of the RandomNameGenerator.
    """

    def __init__(
            self,
            seed_data_path=SEED_DATA_PATH,
            numbers_probabilities=NUMBERS_PROBABILITIES,
    ):
        """
        The constructor of the `RandomNameGenerator` class.

        :param seed_data_path: path to the data based on which the name will be generated.
        :param numbers_probabilities: the probability of occurrence of numbers in the generated word.
        """
        self.seed_data_path = seed_data_path
        self.numbers_probabilities = numbers_probabilities
        self.__base_dict = self.__get_base_dict()

    def generate(self) -> str:
        """
        Generate `EOS` name method.

        :return: `EOS` name str
        """
        mock_name = 'accountnum12'
        return mock_name

    def generate_list(self, num: int) -> list:
        """
        Generate list of `EOS` names method.

        :param num: number of generated names in list.
        :return: `EOS` name
        """
        mock_name = 'accountnum12'
        generated_list = []
        for _ in range(num):
            generated_list.append(mock_name)

        return generated_list

    @property
    def seed_data_path(self) -> str:
        """
        Get `seed_data_path` variable.

        :return: `generation_base_data_path` string value
        """
        return self._seed_data_path

    @seed_data_path.setter
    def seed_data_path(self, value):
        """
        Set `seed_data_path` value and generate new basic dictionary.

        :param value: `seed_data_path` variable value
        """
        self._seed_data_path = value
        self.__base_dict = self.__get_base_dict()

    @property
    def numbers_probabilities(self) -> int:
        """
        Get `numbers_probabilities` variable.

        :return: `numbers_probabilities` int value
        """
        return self._numbers_probabilities

    @numbers_probabilities.setter
    def numbers_probabilities(self, value):
        """
        Set `numbers_probabilities` value.

        :param value: `numbers_probabilities` variable value
        """
        if 0 < value > 1:
            raise ValueError("The numbers probabilities value must be between 1 and 0.")

        self._numbers_probabilities = value

    def __get_base_dict(self) -> defaultdict:
        """
        Rend data from `seed_data_path` and transform it into `dictionary` object
        where the key is the word length.
        """
        with open(self.seed_data_path) as f:
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

    def __repr__(self):
        """
        Debug `repr` method.

        :return: `RandomNameGenerator` object state
        """
        return f'<RandomNameGenerator({self.seed_data_path}, {self.numbers_probabilities})>'
