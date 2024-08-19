def move(no: int, x: int, y: int) -> None:
    """把no个圆盘从第x根柱子移动到第y根柱子"""
    if no > 1:
        move(no - 1, x, 6 - x - y)
    print(f"把[{no}]号圆盘从第{x}根柱子移动到第{y}根柱子")

    if no > 1:
        move(no - 1, 6 - x - y, y)


print("汉诺塔问题")
n = int(input("圆盘数量: "))
move(n, 1, 3)
