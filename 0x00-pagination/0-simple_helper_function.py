#!/usr/bin/env python3
"""
Implement a helper function to compute the index range of a page
"""
import typing as t


def index_range(page: int, page_size: int) -> t.Tuple[int, int]:
    """
    Compute the index range of a page
    """
    start_index = (page - 1) * page_size

    return start_index, start_index + page_size
