from typing import MutableSequence


def sort3(a: MutableSequence[int], idx1: int, idx2: int, idx3: int) -> int:
    """将a[idx1],a[idx2],a[idx3]按升序排序，返回中值的下标"""
    if a[idx2] < a[idx1]:
        a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]:
        a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]:
        a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2


def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    """对a[left] ~ a[right] 进行直接插入排序"""
    for i in range(left + 1, right + 1):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp


def qsort(a: MutableSequence, left: int, right: int) -> None:
    """对a[left] ~ a[right]进行快速排序"""
    if right - left < 9:
        insertion_sort(a, left, right)
    else:
        pl = left
        pr = right
        m = sort3(a, pl, (pl + pr) // 2, pr)
        x = a[m]

        a[m], a[pr - 1] = a[pr - 1], a[m]
        pl += 1
        pr -= 2
        while pl <= pr:
            while a[pl] < x:
                pl += 1
            while a[pr] > x:
                pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1
        if left < pr:
            qsort(a, left, pl)
        if pl < right:
            qsort(a, pl, right)


def quick_sort(a: MutableSequence) -> None:
    qsort(a, 0, len(a) - 1)


if __name__ == '__main__':
    print("快速排序version 2")
    num = int(input("元素个数:"))
    x = [0, ] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]: "))

    quick_sort(x)
    print(x)
    print("已按升序排序")
    for i in range(num):
        print(f"x[{i}]: {x[i]}")
