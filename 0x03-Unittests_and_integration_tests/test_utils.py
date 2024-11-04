#!/usr/bin/env python3
"""
Unit tests for the access_nested_map function and related utilities.
"""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from parameterized import parameterized # type: ignore


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence[Any], expected: Any) -> None:
        """
        Test the access_nested_map function to ensure it returns the expected value.
        
        Args:
            nested_map (Mapping): A dictionary that may contain nested dictionaries.
            path (Sequence): A sequence of keys used to access the required value
                             in the nested dictionary.
            expected (Any): The expected result from accessing the nested map.
        """
        response = access_nested_map(nested_map, path)
        self.assertEqual(response, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence[Any]) -> None:
        """
        Test that access_nested_map raises an exception for invalid paths.
        
        Args:
            nested_map (Mapping): A dictionary that may contain nested dictionaries.
            path (Sequence): A sequence of keys used to access a value that does not exist.
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url: str, test_payload: dict,
                      mock_requests_get) -> None:
        """
        Test that the get_json function returns the expected JSON response.
        
        Args:
            test_url (str): The URL to send the HTTP request to.
            test_payload (dict): The expected JSON response.
            mock_requests_get: Mocked requests.get method for testing.
        """
        mock_requests_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_requests_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the memoization decorator, memoize.
    """
    def test_memoize(self) -> None:
        """
        Test that the memoize decorator caches results as intended.
        """
        class TestClass:
            def a_method(self) -> int:
                return 42

            @memoize
            def a_property(self) -> int:
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once() 
