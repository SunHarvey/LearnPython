from typing import MutableSequence


def qsort(seq: MutableSequence, left: int, right: int) -> None:
    """对a[left] ~ a[right]进行快速排序"""
    pl = left
    pr = right
    x = seq[(left + right) // 2]

    print(f"seq[{left}] ~ seq[{right}]:", *seq[left: right + 1])
    while pl <= pr:
        while seq[pl] < x:
            pl += 1
        while seq[pr] > x:
            pr -= 1
        if pl <= pr:
            seq[pl], seq[pr] = seq[pr], seq[pl]
            pl += 1
            pr -= 1
    if left < pr:
        qsort(seq, left, pr)
    if pl < right:
        qsort(seq, pl, right)


def quick_sort(seq: MutableSequence) -> None:
    """快速排序"""
    qsort(seq, 0, len(seq) - 1)


if __name__ == '__main__':
    print("快速排序")
    num = int(input("元素个数:"))
    ls = [0, ] * num
    for i in range(num):
        ls[i] = int(input(f"x[{i}]:"))

    quick_sort(ls)
    print("已按升序排序")
    print(ls)
    for i in range(num):
        print(f"x[{i}] = {ls[i]}")
