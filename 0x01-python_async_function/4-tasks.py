#!/usr/bin/env python3.8
"""
This module contains a function that creates multiple asyncio.Tasks.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:

    """
    Executes task_wait_random n times and returns a list of the delays.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay for each task.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
