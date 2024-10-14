#!/usr/bin/env python3
"""
This module contains a function that creates an asyncio.Task.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that runs the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The task running the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
