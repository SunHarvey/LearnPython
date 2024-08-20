from typing import MutableSequence


def bubble_sort2(a: MutableSequence) -> None:
    """直接交换排序(第二版:根据交换次数终止程序)"""
    n = len(a)
    for i in range(n - 1):
        exchng = 0
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        if exchng == 0:
            break


if __name__ == '__main__':
    print("直接交换拍下(冒泡排序)")
    num = int(input("元素个数:"))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]:"))
    print(x)

    bubble_sort2(x)
    print("已按升序排序")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
    print(x)
