#!/usr/bin/env python3
""" the utils.access_nested_map function and understand
    its purpose
"""

import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ Implement the TestAccessNestedMap.test_access_nested_map
        method to test that the method returns what it is supposed to
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path_map, result_expec):
        """ Access nested method
        """
        self.assertEqual(access_nested_map(nested_map, path_map), result_expec)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
