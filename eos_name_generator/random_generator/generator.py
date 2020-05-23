"""
Provide an implementation of the RandomNameGenerator interface.
"""
from collections import defaultdict

from eos_name_generator.constants import RANDOM_NAME_GENERATOR_BASE_DATA_PATH
from eos_name_generator.interfaces import BaseGeneratorInterface


class RandomNameGenerator(BaseGeneratorInterface):
    """
    Implementation of the RandomNameGenerator.
    """

    def __init__(self, generation_base_data_path=RANDOM_NAME_GENERATOR_BASE_DATA_PATH):
        self.generation_base_data_path = generation_base_data_path
        self.base_dict = self.__get_base_dict()

    def generate(self) -> str:
        """
        Generate `EOS` name method.

        :return: `EOS` name str
        """
        return ''

    def generate_list(self) -> list:
        """
        Generate list of `EOS` names method.

        :return: list of `EOS` names
        """
        return []

    def __get_base_dict(self) -> defaultdict:
        with open(self.generation_base_data_path) as f:
            data = f.read().splitlines()

        data_dictionary_by_word_len = defaultdict(list)
        for word in data:
            word_len = len(word)
            data_dictionary_by_word_len[word_len].append(word)

        return data_dictionary_by_word_len

    def __repr__(self):
        """
        Debug `repr` method.

        :return: RandomNameGenerator object state
        """
        return '<RandomNameGenerator >'
