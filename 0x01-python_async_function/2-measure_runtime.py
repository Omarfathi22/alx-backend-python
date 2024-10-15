#!/usr/bin/env python3
"""
This module measures the execution time of the wait_n coroutine.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_runtime - function execute async_com 4 times
    Arguments:
        nothing
    Returns:
        the total exection time required to complete the task
    """
   
   
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
