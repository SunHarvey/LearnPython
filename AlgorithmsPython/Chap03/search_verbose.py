from typing import Any, Sequence


def bin_search(a: Sequence[Any], key: Any):
    p_left = 0
    p_right = len(a) - 1
    print("    |", end="")
    for i in range(len(a)):
        print("{i:4}".format(i=i), end="")
    print()
    print("---+" + (4 * len(a) + 2) * "-")

    while True:
        p_center = (p_left + p_right) // 2
        print("    |", end="")
        if p_left != p_center:
            print((p_left * 4 + 1) * " " + "<-" + ((p_center - p_left) * 4) * " " + "+", end="")
        else:
            print((p_center * 4 + 1) * " " + "<+", end="")
        if p_center != p_right:
            print(((p_right - p_center) * 4 - 2) * " " + "->")
        else:
            print("->")

        print("{p_center:3}".format(p_center=p_center), end="")
        for i in range(len(a)):
            print(f"{a[i]:4}", end="")
        print("\n  |")

        if a[p_center] == key:
            return p_center
        elif a[p_center] < key:
            p_left += 1
        else:
            p_right -= 1
        if p_left > p_right:
            break
    return -1


ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
num = 8
print(bin_search(ls, num))
