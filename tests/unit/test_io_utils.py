
"""
Unit tests for assignment4.io_utils module.
"""

from unittest.mock import patch
import pytest
from assignment5.io_utils import get_filehandle, is_gene_file_valid


SAMPLE_GENE_FILE = "C:/Users/coco/PycharmProjects/" \
                   "2/assignment5/assignment5_data"


def test_getfilehandle_oserror():
    """Test if get_filehandle raises OSError for a non-existent file."""
    with pytest.raises(OSError):
        get_filehandle("does_not_exist.txt", "r")


def test_get_filehandle_invalid_mode():
    """Test if get_filehandle raises ValueError for an invalid mode."""
    with pytest.raises(ValueError):
        get_filehandle(file='invalid_file.txt', mode='invalid')


def test_is_gene_file_valid_valid():
    """ Test the is_gene_file_valid function for true value """
    with (
            patch("os.path.exists", return_value=True),
            patch("os.path.isfile", return_value=True),
    ):
        result = is_gene_file_valid(SAMPLE_GENE_FILE)

    assert result is True


def test_is_gene_file_valid_invalid():
    """
       Unit test for the 'is_gene_file_valid' function
        ,when the file does not exist.
    """
    with (
            patch("os.path.exists", return_value=False),
            patch("os.path.isfile", return_value=False),
    ):
        result = is_gene_file_valid(SAMPLE_GENE_FILE)

    assert result is False
