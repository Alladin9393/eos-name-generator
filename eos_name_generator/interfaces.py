"""
Provide implementation of the BaseGenerator interfaces.
"""
from abc import (
    ABC,
    abstractmethod,
)


class BaseGeneratorInterface(ABC):
    """
    Implements BaseGenerator interface.
    """

    @abstractmethod
    def generate(self) -> str:
        """
        Generate `EOS` name.

        :return: `EOS` name
        """

    @abstractmethod
    def generate_list(self, num: int) -> list:
        """
        Generate list of `EOS` names.

        :param num: number of generated names in list.
        :return: `EOS` name
        """
