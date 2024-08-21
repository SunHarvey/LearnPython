from typing import MutableSequence


def partition(seq: MutableSequence) -> MutableSequence:
    """"对数组进行分组并显示"""
    n = len(seq)
    pl = 0
    pr = n - 1
    x = seq[n // 2]

    while pl <= pr:
        while seq[pl] < x:
            pl += 1
        while seq[pr] > x:
            pr -= 1
        if pl <= pr:
            seq[pl], seq[pr] = seq[pr], seq[pl]
            pl += 1
            pr -= 1

    print(f"枢轴的值为{x}")
    print("小于等于枢轴的组")
    print(*seq[0:pl])
    if pl > pr + 1:
        print("等于枢轴的组")
        print(*seq[pr + 1:pl])

    print("大于等于枢轴的组")
    print(*seq[pr + 1:n])

    return seq


if __name__ == "__main__":
    print("对数组进行分组")
    num = int(input("元素个数:"))
    ls = [0, ] * num
    for i in range(num):
        ls[i] = int(input(f"ls[{i}]"))

    partition(ls)
