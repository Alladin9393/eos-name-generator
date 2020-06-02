"""
Provide implementation of the FastRandomChoice interfaces.
"""
from abc import (
    ABC,
    abstractmethod,
)


class FastRandomChoiceInterface(ABC):
    """
    Provide implementation of the FastRandomChoice interfaces.
    """

    @abstractmethod
    def choice(self, seq, p):
        """
        Choose a random element from a non-empty sequence with probabilities list.

        :param seq: non-empty sequence.
        :param p: probabilities according to sequence.
        :return: random element from sequence
        """
