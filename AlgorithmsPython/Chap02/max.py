from typing import Any, Sequence


def max_of(a: Sequence[Any]) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


if __name__ == '__main__':
    print("求数组最大值")
    num = int(input("元素个数:"))
    x = [None] * num
    print(x, type(x))
    for j in range(num):
        x[j] = int(input('x[{}]: '.format(j)))
    print("z最大值为:{}".format(max_of(x)))
