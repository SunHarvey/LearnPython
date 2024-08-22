from typing import MutableSequence


def heap_sort(seq: MutableSequence) -> None:
    def down_heap(seq: MutableSequence, left: int, right: int) -> None:
        """将seq[left] - a[right]堆化"""
        temp = seq[left]
        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and seq[cr] > seq[cl] else cl
            if temp >= seq[child]:
                break
            seq[parent] = seq[child]
            parent = child
        seq[parent] = temp

    n = len(seq)
    for i in range((n - 1) // 2, -1, -1):
        down_heap(seq, i, n - 1)
    for j in range(n - 1, 0, -1):
        seq[0], seq[j] = seq[j], seq[0]
        down_heap(seq, 0, j - 1)


if __name__ == '__main__':
    print("堆排序")
    num = int(input("元素个数:"))
    x = ["", ] * num
    for i in range(num):
        x[i] = int(input(f"x[{i}]"))

    heap_sort(x)
    print("已按升序排序")
    for i in range(num):
        print(f"x[{i}]={x[i]}")
