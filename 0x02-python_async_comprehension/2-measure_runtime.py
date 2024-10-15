#!/usr/bin/env python3
"""A Python module to measure the execution time."""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension



async def measure_runtime() -> float:
    """
    measure_runtime - function to execute async_comprehension 4 times.
    
    Arguments:
        nothing
        
    Returns:
        The total execution time required to complete the task.
    """
    t_start = time.perf_counter()
    task = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*task)
    t_end = time.perf_counter()
    return (t_end - t_start)
