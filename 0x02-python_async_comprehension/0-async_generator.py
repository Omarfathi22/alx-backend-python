#!/usr/bin/env python3
""" 
A Python module that defines an asynchronous generator to yield random floating-point numbers.

This module utilizes the asyncio library to create an asynchronous generator function 
that generates ten random float values between 0 and 10, yielding one value each second.
"""

import random
import asyncio
from typing import Generator

async def async_generator() -> Generator[float, None, None]: # type: ignore
    """
    async_generator - function to loop 10 times
    Arguments:
        no arguments
    Returns:
        nothing
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
