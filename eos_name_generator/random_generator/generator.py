"""
Provide an implementation of the RandomNameGenerator interface.
"""
from eos_name_generator.constants import (
    EOS_NAME_LENGTH,
    NUMBERS_PROBABILITIES,
    RANDOM_PROVIDER_INSTANCE,
    SEED_DATA_PATH,
)
from eos_name_generator.interfaces import BaseGeneratorInterface
from eos_name_generator.random_generator.data_reader import DataReader


class RandomNameGenerator(BaseGeneratorInterface):
    """
    Implementation of the RandomNameGenerator.
    """

    def __init__(
            self,
            seed_data_path=SEED_DATA_PATH,
            numbers_probabilities=NUMBERS_PROBABILITIES,
            random_provider_instance=RANDOM_PROVIDER_INSTANCE,
    ):
        """
        `RandomNameGenerator` constructor.

        :param seed_data_path: path to the data based on which the name will be generated.
        :param numbers_probabilities: the probability of occurrence of numbers in the generated word.
        :param random_provider_instance: the random provider instance.
        """
        self._seed_data_path = seed_data_path
        self.numbers_probabilities = numbers_probabilities
        self.random_provider = random_provider_instance
        self.data_provider = DataReader

    def generate(self) -> str:
        """
        Generate `EOS` name method.

        :return: `EOS` name str
        """
        base_dict_keys = list(self.__base_dict.keys())
        base_word_len = self.random_provider.choice(base_dict_keys, p=self.__probabilities_len_base_word)
        additional_word_len = EOS_NAME_LENGTH - base_word_len

        base_words = self.__base_dict.get(base_word_len)
        additional_alphabet_words = []
        if additional_word_len in self.__base_dict:
            additional_alphabet_words = self.__base_dict.get(additional_word_len)

        name = self.__get_random_name(base_words, additional_alphabet_words)

        return name

    def generate_list(self, num: int) -> list:
        """
        Generate list of `EOS` names method.

        :param num: number of generated names in list.
        :return: `EOS` name
        """
        generated_list = []
        for _ in range(num):
            name = self.generate()
            generated_list.append(name)

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
        Set `seed_data_path` value and generate new basic dictionary and probabilities word length.

        :param value: `seed_data_path` variable value
        """
        self._seed_data_path = value
        self.data_provider.data_path = value
        self.__base_dict = self.data_provider.get_dictionary_by_word_len()
        self.__probabilities_len_base_word = self.__get_probabilities_len_base_word()

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

    @property
    def random_provider(self):
        """
        Get `random_provider` variable.

        :return: `random_provider` instance.
        """
        return self._random_provider

    @random_provider.setter
    def random_provider(self, value):
        """
        Set `random_provider` value.

        :param value: `random_provider` instance.
        """
        random_provider_dir = dir(value)
        required_methods = ['choice', 'randint']

        for method_name in required_methods:
            if method_name not in random_provider_dir:

                error_message = f'The interface `random_provider` does not contain {method_name} method.'
                raise AttributeError(error_message)

        self._random_provider = value

    @property
    def data_provider(self):
        """
        Get `data_provider` variable.

        :return: `data_provider` instance.
        """
        return self._data_provider

    @data_provider.setter
    def data_provider(self, value):
        """
        Set `data_provider` variable.

        :param value: `data_provider` variable value.
        """
        data_provider_dir = dir(value)
        required_method = 'get_dictionary_by_word_len'

        if required_method not in data_provider_dir:

            error_message = f'The interface `data_provider` does not contain {required_method} method.'
            raise AttributeError(error_message)

        self._data_provider = value(self.seed_data_path)
        self.__base_dict = self.data_provider.get_dictionary_by_word_len()
        self.__probabilities_len_base_word = self.__get_probabilities_len_base_word()

    def __get_random_name(self, base_words, additional_alphabet_words) -> str:
        """
        Generate random name based on `base_words` and `additional_alphabet_words`.

        :param base_words: list of words on the basis of which the name will be created
        :param additional_alphabet_words: additional words to be added to the base word
        :return: random name string
        """
        base_word_random_index = self.random_provider.randint(0, len(base_words) - 1)
        base_word = base_words[base_word_random_index]
        additional_alphabet_words_len = len(additional_alphabet_words)
        additional_word_alphabet_probability = self.__get_probability_alphabet_additional_word(
            additional_alphabet_words_len,
        )

        numbers_probabilities = self.numbers_probabilities if additional_word_alphabet_probability else 1
        additional_words_probabilities = [additional_word_alphabet_probability, numbers_probabilities]
        is_additional_alphabet_word = self.random_provider.choice([True, False], p=additional_words_probabilities)

        additional_word = ''
        if is_additional_alphabet_word:
            additional_word_random_index = self.random_provider.randint(0, additional_alphabet_words_len - 1)
            additional_word = additional_alphabet_words[additional_word_random_index]
        else:
            additional_numbers_len = EOS_NAME_LENGTH - len(base_word)
            for _ in range(additional_numbers_len):
                additional_char = str(self.random_provider.randint(1, 5))
                additional_word += additional_char

        random_name = base_word + additional_word
        return random_name

    def __get_probabilities_len_base_word(self) -> list:
        """
        Get probabilities list of the base word length based on word frequency.

        :return: probabilities list
        """
        probabilities = []
        base_dict_len = 0

        for key in self.__base_dict:
            word_count = len(self.__base_dict.get(key))
            base_dict_len += word_count
            probabilities.append(word_count)

        probabilities = [word_count / base_dict_len for word_count in probabilities]

        return probabilities

    def __get_probability_alphabet_additional_word(self, additional_alphabet_words_len) -> int:
        """
        Get probability of the additional word alphabet.

        Get probability of the additional word alphabet based on `numbers_probabilities`
        and `additional_alphabet_words_len`.

        :return: probabilities list
        """
        additional_words_probability = 0
        if additional_alphabet_words_len:
            additional_words_probability = 1 - self.numbers_probabilities

        return additional_words_probability

    def __repr__(self):
        """
        Debug `repr` method.

        :return: `RandomNameGenerator` object state
        """
        return f'<RandomNameGenerator({self.seed_data_path}, {self.numbers_probabilities}, {self.random_provider})>'
