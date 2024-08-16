from __future__ import annotations
from typing import Any, Type
import hashlib


class Node:
    """数组散列表的节点"""

    def __init__(self, key: Any, value: Any, next_node: Node) -> None:
        self.key = key
        self.value = value
        self.next_node = next_node


class ChainedHash:
    """通过散列表类实现拉链法"""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        """求散列值"""
        if isinstance(key, int):
            return key % self.capacity
        return int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity

    def search(self, key: Any) -> Any:
        """查找关键字为key的(返回值)"""
        get_hash = self.hash_value(key)
        p = self.table[get_hash]
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        return None

    def add(self, key: Any, value: Any) -> bool:
        """插入关键字为key,值为value的元素"""
        get_hash = self.hash_value(key)
        p = self.table[get_hash]
        while p is not None:
            if p.key == key:
                return False
            p = p.next_node
        temp = Node(key, value, self.table[get_hash])
        self.table[get_hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        """删除关键字为key的元素"""
        get_hash = self.hash_value(key)
        p = self.table[get_hash]
        pp = None
        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[get_hash] = p.next_node
                else:
                    pp.next_node == p.next_node
                return True
            pp = p
            p = p.next_node
        return False

    def dump(self) -> None:
        """转存散列表"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end="")
            while p is not None:
                print(f"  -> {p.key}  ({p.value})", end="")
                p = p.next_node
            print()
