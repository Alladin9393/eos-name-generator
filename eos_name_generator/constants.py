"""
Provide constants for BaseGenerator interface.
"""
from os.path import dirname

from eos_name_generator.utils import FastRandomChoice

EOS_NAME_LENGTH = 12
SEED_DATA_PATH = dirname(__file__) + '/' + 'random_generator/seed_data/nounlist.txt'
NUMBERS_PROBABILITIES = 0.1
RANDOM_PROVIDER_INSTANCE = FastRandomChoice()
