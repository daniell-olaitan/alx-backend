#!/usr/bin/env python3
"""
Implement a base class for Caching
"""
from basic_caching import BaseCaching
import typing as t


class BasicCache(BaseCaching):
    """
    Implement a caching system
    """
    def put(self, key: str, item: str) -> None:
        """
        Put an item in the cache
        """
        if (key is not None) and (item is not None):
            self.cache_data.update({key: item})

    def get(self, key: str) -> str:
        """
        Get an item from the cache
        """
        if key is None:
            return None

        return self.cache_data.get(key, None)
