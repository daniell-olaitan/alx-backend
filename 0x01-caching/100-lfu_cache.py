#!/usr/bin/env python3
"""
Implement a class for LFU cache policy
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Implement LFU cache policy
    """
    def __init__(self):
        """
        Initialization method
        """
        super().__init__()
        self._item_age = {}

    def _compute_order_freq(self) -> None:
        """
        Compute the order and frequency of the cache items
        """
        self._item_age = dict(
            sorted(self._item_age.items(), key=lambda x: x[1])
        )

    def put(self, key: str, item: str) -> None:
        """
        Put an item in the cache
        """
        if (key is not None) and (item is not None):
            self.cache_data.update({key: item})
            if len(self.cache_data) > self.MAX_ITEMS:
                k = tuple(self._item_age.keys())[0]
                del self.cache_data[k]
                del self._item_age[k]
                print(f"DISCARD: {k}")

            if key in self._item_age:
                count = self._item_age[key] + 1
                del self._item_age[key]
                self._item_age.update({key: count})
            else:
                self._item_age.update({key: 0})

            self._compute_order_freq()

    def get(self, key: str) -> str:
        """
        Get an item from the cache
        """
        if key is None:
            return None

        item = self.cache_data.get(key, None)
        if item:
            count = self._item_age[key] + 1
            del self._item_age[key]
            self._item_age.update({key: count})
            self._compute_order_freq()

        return item
