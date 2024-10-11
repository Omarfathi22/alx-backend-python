#!/usr/bin/env python3
"""
Module that provides a function to sum a mixed list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a mixed list of integers and floats.

   
    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and floats to sum.

    Returns:
        float: The sum of the numbers in the mixed list.
    """
    return float(sum(mxd_lst))
