#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import typing as t


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
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> t.Dict[int, t.List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(
        self,
        index: int = None,
        page_size: int = 10
    ) -> t.Dict:
        """
        Perform deletion-resilient pagination on the database
        """
        dataset = self.indexed_dataset()
        data_len = len(dataset)
        assert index is not None and index < data_len

        data = []
        current_index = index
        count = 0
        while count < page_size and current_index < data_len:
            data_bit = dataset.get(current_index, None)
            if data_bit:
                data.append(data_bit)
                count += 1

            current_index += 1

        return {
            'index': index,
            'page_size': count,
            'next_index': current_index if current_index < data_len else None,
            'data': data
        }


server = Server()

server.indexed_dataset()

try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")


index = 3
page_size = 2

print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 1- request first index
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next index
print(server.get_hyper_index(res.get('next_index'), page_size))

# 3- remove the first index
del server._Server__indexed_dataset[res.get('index')]
print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 4- request again the initial index -> the first data retreives is not the same as the first request
print(server.get_hyper_index(index, page_size))

# 5- request again initial next index -> same data page as the request 2-
print(server.get_hyper_index(res.get('next_index'), page_size))
