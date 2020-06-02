"""
Provide an implementation of the FastRandomChoice interface.
"""
import random

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
            ValueError('`seq` and `p` must have same size')

        is_probabilities_positive = all(i >= 0 for i in p)
        if not is_probabilities_positive:
            raise ValueError('Probabilities are not non-negative')

        probabilities_sum = sum(p)
        if 0.99 < probabilities_sum > 1.01:
            print(probabilities_sum)
            raise ValueError('Probabilities do not sum to 1')

        random_element = ''
        is_element_fount = True
        while is_element_fount:
            candidate_element = super().choice(seq=seq)
            candidate_probability_index = seq.index(candidate_element)
            candidate_probability = p[candidate_probability_index]

            random_probability = self.random()
            if candidate_probability >= random_probability:
                random_element = candidate_element
                is_element_fount = False

        return random_element
