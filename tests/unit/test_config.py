"""
This module contains unit tests
 for the functions in the 'assignment5.config' module.

Functions:
- test_get_directory_for_unigene():
                             Tests the 'get_directory_for_unigene' function.
- test_get_extension_for_unigene():
                             Tests the 'get_extension_for_unigene' function.
- test_get_keywords_for_hosts():
                             Tests the 'get_keywords_for_hosts' function.
- test_get_error_string_4_exception_type():
                        Tests the 'get_error_string_4_exception_type' function.
"""
import pytest
from assignment5.config import (get_directory_for_unigene, get_extension_for_unigene,
                                get_keywords_for_hosts, get_error_string_4_exception_type)


def test_get_directory_for_unigene():
    "Tests the 'get_directory_for_unigene' function."
    result = get_directory_for_unigene()
    assert isinstance(result, str)
    assert result.startswith("C:/Users/coco/PycharmProjects/"
                             "2/assignment5/assignment5_data")


def test_get_extension_for_unigene():
    """Tests the 'get_extension_for_unigene' function"""
    result = get_extension_for_unigene()
    assert isinstance(result, str)
    assert result == "unigene"


def test_get_keywords_for_hosts():
    """Tests the 'get_keywords_for_hosts' function"""
    result = get_keywords_for_hosts()
    assert isinstance(result, dict)
    assert "homo sapiens" in result
    assert result["homo sapiens"] == "Homo_sapiens"
    # Add more specific test cases based on your mappings


def test_get_error_string_4_exception_type():
    """ Tests the 'get_error_string_4_exception_type' function."""
    exception_type = "ValueError"
    result = get_error_string_4_exception_type(exception_type)
    assert isinstance(result, str)
    assert "Error: ValueError occurred." in result


if __name__ == "__main__":
    pytest.main(["-v"])
