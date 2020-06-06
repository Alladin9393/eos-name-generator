"""
Provide constants for command line interface.
"""
from numpy import random

from eos_name_generator.utils import FastRandomChoice

PASSED_EXIT_FROM_COMMAND_CODE = 0
FAILED_EXIT_FROM_COMMAND_CODE = -1
INCORRECT_ENTERED_COMMAND_CODE = 2

NUMPY_RANDOM_PROVIDER = random
FAST_RANDOM_CHOICE_PROVIDER = FastRandomChoice()
NUMBERS_PROBABILITY = 0.1
