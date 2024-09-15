#!/usr/bin/env python3
"""
Implement a Server base class to test pagination
"""
import csv
import typing as t


def index_range(page: int, page_size: int) -> t.Tuple[int, int]:
    """
    Compute the index range of a page
    """
    start_index = (page - 1) * page_size

    return start_index, start_index + page_size


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    @property
    def dataset(self) -> t.List[t.List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> t.List[t.List]:
        """
        Get the pagination of a page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        if end_index > len(self.dataset):
            return []

        return self.dataset[start_index:end_index]
