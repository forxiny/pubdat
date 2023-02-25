"""
Utility functions for processing Reddit data from Pushshift API and monthly archives.
"""

from pathlib import Path
import polars as pl
from datetime import datetime
import time
import sys


def get_archive_filepaths(folder):
    """
    Get file paths for all json files in the specified folder

    :param folder: path to folder holding decompressed pushshift monthly files
    :return: generator of file paths
    """

    filepaths = Path(folder).glob("*.json")

    return filepaths


def json_to_dataframe(infile):
    """
    Loads and filters a Pushshift json archive and returns subset of data as polars dataframe

    :param infile: Path to a json file
    :return: polars dataframe
    """
    columns_to_keep = [
        'author',
        'author_created_utc',
        'author_flair_text',
        'author_fullname',
        'created_utc',
        'domain',
        'id',
        'locked',
        'name',
        'num_comments',
        'num_crossposts',
        'permalink',
        'retrieved_utc',
        'score',
        'selftext',
        'subreddit',
        'subreddit_id',
        'subreddit_subscribers',
        'subreddit_type',
        'title',
        'total_awards_received',
        'upvote_ratio',
        'url']

    filename = Path(infile).stem

    df = pl.scan_ndjson(infile) \
        .filter((pl.col('author') != '[deleted]') & (pl.col('selftext') != None) & (pl.col('selftext') != '')) \
        .select(columns_to_keep) \
        .collect()

    return df, filename



