#!/usr/bin/env python3
"""
Module that provides a function to safely get a value from a dictionary.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, 
                     default: Union[T, None] = None) -> Union[T, Any]:
    """
    Return the value associated with a key in a dictionary or a default value.

    Args:
        dct (Mapping[Any, T]): The dictionary to search.
        key (Any): The key to look for.
        default (Union[T, None], optional): The default value to return if the key is not found. 
                                            Defaults to None.

    Returns:
        Union[T, Any]: The value associated with the key or the default value.
    """
    if key in dct:
        return dct[key]
    return default
