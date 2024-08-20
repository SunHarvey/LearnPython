from typing import MutableSequence


def shell_sort(seq: MutableSequence) -> None:
    n = len(seq)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = seq[i]
            while j >= 0 and seq[j] > tmp:
                seq[j + h] = seq[j]
                j -= h
            seq[j + h] = tmp
        h //= 2


if __name__ == '__main__':
    print("希尔排序")
    num = int(input("元素个数: "))
    x = [0, ] * num

    for i in range(num):
        x[i] = int(input(f"x[{i}]:"))

    shell_sort(x)

    print("已按升序排序")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")
