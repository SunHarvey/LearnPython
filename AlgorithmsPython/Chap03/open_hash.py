from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib


class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2


class Bucket:
    """组成散列表的桶"""

    def __init__(self, key: Any = None, value: Any = None, stat: Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """为所有字段设置值"""
        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:
        """设置·属性"""
        self.stat = stat


class OpenHash:
    """实现开放地址法的散列值"""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    def hash_value(self, key: Any) -> int:
        """求散列值"""
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16) % self.capacity

    def rehash_value(self, key: Any) -> int:
        """求再散列值"""
        return (self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        """查找关键字为key的桶"""
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(key)
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        """查找关键字为key的元素"""
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return None

    def add(self, key: Any, value: Any) -> bool:
        """添加关键字为key,值为value的元素"""
        if self.search(key) is not None:
            return False
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.OCCUPIED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(key)
            p = self.table[hash]
        return False

    def remove(self, key: Any) -> int:
        """删除关键字为key的元素"""
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        """转存散列表"""
        for i in range(self.capacity):
            print(f'{i:2}  ', end="")
            if self.table[i].stat == Status.OCCUPIED:
                print(f"{self.table[i].key}  ({self.table[i].value})")
            elif self.table[i].stat == Status.EMPTY:
                print("--- 未转存 ---")
            elif self.table[i].stat == Status.DELETED:
                print("--- 已删除 ---")
