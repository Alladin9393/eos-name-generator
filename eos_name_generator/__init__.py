"""Top-level module for `EOS` name generator.

This module generate random name which suits for `eosio blockchain` name
conversation.

The module provides 3 methods to generate a name:
    - random name generation based in a ready-made data (word dictionary)
    - markov chain text generation
    - recurrent neural network text generation
"""
from eos_name_generator.random_generator.generator import RandomNameGenerator

__version__ = "0.1.0"
__version_info__ = tuple(
    int(i) for i in __version__.split(".") if i.isdigit()
)
