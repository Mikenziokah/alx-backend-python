#!/usr/bin/env python3
""" function multplier that multplies floats
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float.
    """
    return lambda x: x * multiplier
