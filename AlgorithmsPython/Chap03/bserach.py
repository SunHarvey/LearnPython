from typing import Any, Sequence


def bin_search(a: Sequence, key: Any):
    p_left = 0
    p_right = len(a) - 1
    while True:
        p_center = (p_left + p_right) // 2
        if a[p_center] == key:
            return p_center
        elif a[p_center] < key:
            p_left = p_center + 1
        else:
            p_right = p_center - 1
        if p_left > p_right:
            break
    return -1


if __name__ == "__main__":
    number = int(input("元素个数: "))
    x = [None] * number
    print("请按照升序输入数据")
    x[0] = int(input('x[0]:'))
    for i in range(1, number):
        while True:
            x[i] = int(input('x[{}]:'.format(i)))
            if x[i] > x[i - 1]:
                break
    ky = int(input('目标值:'))
    idx = bin_search(x, ky)

    if idx == -1:
        print("不存在与该值相等的元素")
    else:
        print("元素下标为x[{}]".format(idx))
