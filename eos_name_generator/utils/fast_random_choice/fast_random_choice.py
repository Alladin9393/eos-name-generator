"""
Provide an implementation of the FastRandomChoice interface.
"""
import random

import numpy as np

from eos_name_generator.utils.fast_random_choice.interfaces import FastRandomChoiceInterface


class FastRandomChoice(random.Random, FastRandomChoiceInterface):
    """
    Implementation of the FastRandomChoice.
    """

    def choice(self, seq, p):
        """
        Choose a random element from a non-empty sequence with probabilities list.

        :param seq: non-empty sequence.
        :param p: probabilities according to sequence.
        :return: random element from sequence
        """
        sequence_len = len(seq)
        if not sequence_len:
            raise IndexError('Cannot choose from an empty sequence')

        if sequence_len != len(p):
            raise ValueError('`seq` and `p` must have same size')

        is_probabilities_positive = all(i >= 0 for i in p)
        if not is_probabilities_positive:
            raise ValueError('Probabilities are not non-negative')

        probabilities_sum = sum(p)
        if 0.99 > probabilities_sum < 1.01:
            raise ValueError('Probabilities do not sum to 1')

        element_index = self.multidimensional_shifting(probabilities=p)
        random_element = seq[element_index]

        return random_element

    @staticmethod
    def multidimensional_shifting(probabilities: list) -> int:
        """
        Get the most probable element from probabilities sequence.

        This method is a direct replacement for slow cycle python loops.
        :param probabilities: probabilities list.
        :return: probability index.
        """
        # replicate probabilities as many times
        replicated_probabilities = np.tile(probabilities, (1, 1))
        # get random shifting numbers & scale them correctly
        random_shifts = np.random.random(replicated_probabilities.shape)
        random_shifts /= random_shifts.sum(axis=1)[:, np.newaxis]
        # shift by numbers & find largest (by finding the smallest of the negative)
        shifted_probabilities = random_shifts - replicated_probabilities
        index_list = np.argpartition(shifted_probabilities, 1, axis=1)[:, :1]

        index = int(index_list)
        return index
