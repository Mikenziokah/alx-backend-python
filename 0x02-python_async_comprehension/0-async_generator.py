#!/usr/bin/env python3
"""async_generator that takes no arguments
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Loop 10 times waiting 1 second and yield a random
        number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
