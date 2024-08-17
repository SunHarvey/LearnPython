from typing import Any


class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.queue = [None] * capacity

    def __len__(self) -> int:
        """返回已经入队的数据个数"""
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no == self.capacity

    def enqueue(self, x: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full('Queue is full')
        self.queue[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def dequeue(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty('Queue is empty')
        x = self.queue[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty('Queue is empty')
        return self.queue[self.front]

    def find(self, value: Any) -> Any:
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.queue[idx] == value:
                return idx
        return -1

    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.queue[idx] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value) or False

    def clear(self) -> None:
        if self.is_empty():
            print("Queue is empty")
        else:
            for i in range(self.no):
                print(self.queue[(i + self.front) % self.capacity], end=" ")
            print()

    def dump(self) -> None:
        if self.is_empty():
            print("队列为空")
        else:
            for i in range(self.no):
                print(self.queue[(i + self.front) % self.capacity], end=" ")
            print()
