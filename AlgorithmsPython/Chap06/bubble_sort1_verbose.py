from typing import MutableSequence


def bubble_sort_verbose(a: MutableSequence) -> None:
    """直接显示交换排序"""
    ccnt = 0
    scnt = 0
    n = len(a)
    for i in range(n - 1):
        print(f"第{i + 1}趟排序")
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(f"{a[m]:2}" + (" " if m != j - 1 else " +" if a[j - 1] > a[j] else " -"), end="")
            print(f"{a[n - 1]:2}")
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
        for m in range(0, n - 1):
            print(f"{a[m]:2}", end="  ")
        print(f"{a[n - 1]:2}")
    print(f"比较次数为{ccnt}")
    print(f"交换次数为{scnt}")


if __name__ == '__main__':
    print("直接交换拍下(冒泡排序)")
    num = int(input("元素个数:"))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]:"))
    print(x)

    bubble_sort_verbose(x)
    print("已按升序排序")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
    print(x)
