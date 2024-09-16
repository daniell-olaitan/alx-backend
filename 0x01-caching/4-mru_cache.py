#!/usr/bin/env python3
"""
Implement a class for MRU caching policy
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Implement a LRU caching policy
    """
    def __init__(self):
        """
        Initialization method
        """
        super().__init__()
        self._item_age = []

    def put(self, key: str, item: str) -> None:
        """
        Put an item in the cache
        """
        if (key is not None) and (item is not None):
            self.cache_data.update({key: item})
            if len(self.cache_data) > self.MAX_ITEMS:
                k = self._item_age.pop()
                del self.cache_data[k]
                print(f"DISCARD: {k}")

            if key in self._item_age:
                self._item_age.remove(key)

            self._item_age.append(key)

    def get(self, key: str) -> str:
        """
        Get an item from the cache
        """
        if key is None:
            return None

        item = self.cache_data.get(key, None)
        if item:
            self._item_age.remove(key)
            self._item_age.append(key)

        return item
