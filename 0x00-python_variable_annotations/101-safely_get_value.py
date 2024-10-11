#!/usr/bin/env python3


from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[T, None]:
    """Safely get a value from a dictionary.

    Args:
        dct (Mapping[Any, T]): The dictionary to search.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): The default value
        to return if the key is not found. Defaults to None.

    Returns:
        Union[T, None]: The value associated with the key
        if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
