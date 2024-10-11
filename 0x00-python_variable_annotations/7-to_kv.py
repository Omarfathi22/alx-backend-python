#!/usr/bin/env python3
"""
Module that provides a function to convert a key and a value to a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple containing a string and the square of a number.

    Args:
        k (str): The string key.
        v (Union[int, float]): The int or float value to be squared.

    Returns:
        Tuple[str, float]: A tuple with the string and the square of the value.
    """
    return (k, float(v ** 2))
