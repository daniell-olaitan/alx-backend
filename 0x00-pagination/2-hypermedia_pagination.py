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
        """
        Initialization method
        """
        self.__dataset = None

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
        dataset = self.dataset()
        if end_index > len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> t.List[t.List]:
        """
        Implement the hypermedia pagination of the server
        """
        data = self.get_page(page, page_size)
        dataset = self.dataset()
        _, end_index = index_range(page, page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if len(dataset) > end_index else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': -(-len(dataset) // page_size)
        }

server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))
