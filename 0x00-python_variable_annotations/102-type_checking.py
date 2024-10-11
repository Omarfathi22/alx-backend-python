#!/usr/bin/env python3
"""
Module that provides a function to zoom in on an array.
"""

from typing import List, Tuple

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Return a new list that repeats each element of the input list a given number of times.

    Args:
        lst (Tuple[int, ...]): The list of integers to zoom.
        factor (int, optional): The number of times to repeat each element. Defaults to 2.

    Returns:
        List[int]: A new list with the zoomed elements.
    """
    zoomed_in: List[int] = [
        item for item in lst for _ in range(factor)
    ]
    return zoomed_in

# Example usage
array = (12, 72, 91)  # Changed to a tuple for consistency with the type annotation
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
