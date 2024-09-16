#!/usr/bin/env python3
"""
Implement a class for LRU caching policy
"""
from base_caching import BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """
    Implement a LRU caching policy
    """
    def __init__(self):
        """
        Initialization method
        """
        super().__init__()
        self._item_age = deque([], maxlen=self.MAX_ITEMS)

    def put(self, key: str, item: str) -> None:
        """
        Put an item in the cache
        """
        if (key is not None) and (item is not None):
            self.cache_data.update({key: item})
            if len(self.cache_data) > self.MAX_ITEMS:
                k = self._item_age.popleft()
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

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
