#!/usr/bin/env python3
"""
Implement a class for FIFO caching policy
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Implement a FIFO caching policy
    """
    def put(self, key: str, item: str) -> None:
        """
        Put an item in the cache
        """
        if (key is not None) and (item is not None):
            if key in self.cache_data:
                del self.cache_data[key]

            self.cache_data.update({key: item})
            if len(self.cache_data) > self.MAX_ITEMS:
                k = list(self.cache_data.keys())[0]
                del self.cache_data[k]
                print(f"DISCARD: {k}")

    def get(self, key: str) -> str:
        """
        Get an item from the cache
        """
        if key is None:
            return None

        return self.cache_data.get(key, None)
