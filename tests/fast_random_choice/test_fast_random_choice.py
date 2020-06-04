"""
Provide tests for FastRandomChoice.
"""
import random

import pytest

from eos_name_generator.utils import FastRandomChoice


def test_random_choice():
    """
    Case: test random choice from list.
    Expect: element is returned.
    """
    infimum = -10_000
    supremum = 10_000
    number_quantity = abs(infimum) + abs(supremum)

    fast_random = FastRandomChoice()
    numbers = list(range(infimum, supremum))
    numbers_probabilities = [1 / number_quantity] * number_quantity
    random_number = fast_random.choice(seq=numbers, p=numbers_probabilities)

    assert infimum <= random_number <= supremum


def test_random_choice_with_big_range():
    """
    Case: test random choice with a lot of elements.
    Expect: random choice is returned.
    """
    infimum = -10_000
    supremum = 10_000
    number_quantity = abs(infimum) + abs(supremum)

    fast_random = FastRandomChoice()
    numbers = list(range(infimum, supremum))
    numbers_probabilities = [1 / number_quantity] * number_quantity
    random_number = fast_random.choice(seq=numbers, p=numbers_probabilities)

    assert infimum <= random_number <= supremum


def test_random_choice_collision_with_uniform_distribution():
    """
    Case: test random choice collision number.
    Expect: elements is returned.
    """
    accuracy = 0.15
    tests_number = 10_00
    infimum = -1_000
    supremum = 1_000
    number_quantity = abs(infimum) + abs(supremum)

    fast_random = FastRandomChoice()
    numbers = list(range(infimum, supremum))
    numbers_probabilities = [1 / number_quantity] * number_quantity
    random_numbers = []

    for _ in range(tests_number):
        random_numbers.append(fast_random.choice(seq=numbers, p=numbers_probabilities))

    random_numbers_set = set(random_numbers)
    error_range = len(random_numbers) - len(random_numbers_set)

    assert error_range < accuracy * number_quantity


def test_random_choice_with_one_true_element():
    """
    Case: test random choice with zeros probabilities and one true element.
    Expect: one element same times is returned.
    """
    tests_number = 10_00
    infimum = -1_000
    supremum = 1_000
    number_quantity = abs(infimum) + abs(supremum)

    fast_random = FastRandomChoice()
    numbers = list(range(infimum, supremum))
    numbers_probabilities = [0] * number_quantity
    random_index = random.randint(infimum, supremum)
    numbers_probabilities[random_index] = 1

    random_numbers = []

    for _ in range(tests_number):
        random_numbers.append(fast_random.choice(seq=numbers, p=numbers_probabilities))

    random_numbers_set = set(random_numbers)

    assert len(random_numbers_set) == 1


def test_random_choice_with_empty_sequence():
    """
    Case: test random choice with empty sequence.
    Expect: cannot choose from an empty sequence error message.
    """
    infimum = -10_000
    supremum = 10_000
    number_quantity = abs(infimum) + abs(supremum)
    numbers = []

    fast_random = FastRandomChoice()
    numbers_probabilities = [0] * number_quantity
    random_index = random.randint(infimum, supremum)
    numbers_probabilities[random_index] = 1

    with pytest.raises(IndexError):
        fast_random.choice(seq=numbers, p=numbers_probabilities)


def test_random_choice_with_different_lengths_sequence_and_probabilities():
    """
    Case: test random choice with different lengths sequence and probabilities.
    Expect: `seq` and `p` must have same size error message.
    """
    infimum = -10_000
    supremum = 10_000
    number_quantity = abs(infimum) + abs(supremum)

    fast_random = FastRandomChoice()
    numbers = list(range(infimum, supremum))
    numbers_probabilities = [0] * (number_quantity - 1)
    random_index = random.randint(infimum, supremum - 1)
    numbers_probabilities[random_index] = 1

    with pytest.raises(ValueError):
        fast_random.choice(seq=numbers, p=numbers_probabilities)


def test_random_choice_with_negative_probability():
    """
    Case: test random choice with negative probability.
    Expect: probabilities are not non-negative error message.
    """
    infimum = -10_000
    supremum = 10_000
    number_quantity = abs(infimum) + abs(supremum)

    fast_random = FastRandomChoice()
    numbers = list(range(infimum, supremum))
    numbers_probabilities = [0] * number_quantity
    random_index = random.randint(infimum, supremum)
    numbers_probabilities[random_index] = -1

    with pytest.raises(ValueError):
        fast_random.choice(seq=numbers, p=numbers_probabilities)


def test_random_choice_with_invalid_probability_sum():
    """
    Case: with the sum of the probabilities less than one.
    Expect: probabilities do not sum to 1 error message.
    """
    infimum = -10_000
    supremum = 10_000
    number_quantity = abs(infimum) + abs(supremum)

    fast_random = FastRandomChoice()
    numbers = list(range(infimum, supremum))
    numbers_probabilities = [0] * number_quantity
    random_index = random.randint(infimum, supremum)
    numbers_probabilities[random_index] = 0.5

    with pytest.raises(ValueError):
        fast_random.choice(seq=numbers, p=numbers_probabilities)
