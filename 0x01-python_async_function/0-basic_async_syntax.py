#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay.
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:

    """
    async_generator - function to loop 10 times
    Arguments:
        no arguments
    Returns:
        nothing
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
