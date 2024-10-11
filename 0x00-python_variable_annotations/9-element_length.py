#!/usr/bin/env python3
"""
Module that provides a function to compute the length of each
element in an iterable.
"""

from typing import Iterable, Sequence, List, Tuple



def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    
    Return a list of tuples with each 
    element and its length.

    Args:
        
        lst (Iterable[Sequence]): An iterable of 
        sequences (like lists or strings).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing an 
        element and its length.
    """
    return [(i, len(i)) for i in lst]
