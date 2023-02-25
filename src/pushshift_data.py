"""
Utility functions for processing Reddit data from Pushshift API and monthly archives.
"""

from pathlib import Path
import polars as pl

def get_archive_filepaths(folder):
    """
    Get file paths for all json files in the specified folder

    :param folder: path to folder holding decompressed pushshift monthly files
    :return: generator of file paths
    """

    filepaths = Path(folder).glob("*.json")

    return filepaths


