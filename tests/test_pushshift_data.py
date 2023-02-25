"""
Tests related to the pushshift_data.py module
"""

import src.pushshift_data as psh_data

def test_get_archive_filepaths():

    assert "get_archive_filepaths" in dir(psh_data)
