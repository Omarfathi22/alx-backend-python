#!/usr/bin/env python3
"""
Module that provides a function to sum a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats to sum.

    Returns:
        float: The sum of the floats in the input list.
    """
    return sum(input_list)
