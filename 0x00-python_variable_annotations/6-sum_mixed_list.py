#!/usr/bin/env python3
"""function sum list that takes in mixed lists"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """return the mixed list"""
    return sum(mxd_list)
