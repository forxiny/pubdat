"""
Tests related to the pushshift_data.py module
"""

import src.pushshift_data as psh_data
import types

def test_get_archive_filepaths():
    """
    check if get_archive_filepaths returns a generator object
    :return: bool
    """
    assert isinstance(psh_data.get_archive_filepaths("E:/"), types.GeneratorType )
