#!/usr/bin/env python3
""" function floor"""


def floor(n: float) -> int:
    """returns floor of the float"""
    return int(n) if n >= 0 else int(n) - 1
