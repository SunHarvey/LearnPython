from typing import MutableSequence


def shaker_sort(a: MutableSequence) -> None:
    """鸡尾酒排序(双向冒泡排序)"""
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last

        for j in range(left, right):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last


if __name__ == '__main__':
    print("直接交换拍下(冒泡排序)")
    num = int(input("元素个数:"))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]:"))
    print(x)

    shaker_sort(x)
    print("已按升序排序")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
    print(x)
