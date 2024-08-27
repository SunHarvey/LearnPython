from __future__ import annotations
from typing import Any, Type


class Node:
    """二叉查找数的节点"""

    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    """二叉查找树"""

    def __init__(self):
        self.root = None

    def search(self, key: Any) -> None:
        """查找关键字为key的节点"""
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key: Any, value: Any) -> bool:
        """插入关键字为key,值为value的节点"""

        def add_node(node: Node, key: Any, value: Any):
            """向以node为根的子数中插入关键字为key,值为value的节点"""
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        """删除关键字为key的节点"""
        p = self.root
        parent = None
        is_left_child = True
        while True:
            if p is None:
                return False
            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right
        if p.left is None:
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.left
        else:
            parent = p
            left = p.left
            is_right_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_right_child = False
            p.key = left.key
            p.value = left.value
            if is_right_child:
                parent.left = left.left
            else:
                parent.right = left.right
        return True

    def dump(self, reverse=False):

        def print_subtree(node: Node):
            """按照关键字升序显示以node为根的子树的节点"""
            if node is not None:
                print_subtree(node.left)
                print(f"{node.key} {node.value}")
                print_subtree(node.right)

        def print_subtree_rev(node: Node):
            """按照关键字降序显示以node为根的子数的节点"""
            if node is not None:
                print_subtree_rev(node.right)
                print(f"{node.key} {node.value}")
                print_subtree_rev(node.left)

        print_subtree(self.root) if reverse else print_subtree(self.root)

    def min_key(self):
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self):
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key
