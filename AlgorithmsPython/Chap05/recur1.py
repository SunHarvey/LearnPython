def recur(n: int) -> int:
    """真正递归函数"""
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)
        print()


x = int(input("请输入一个整数: "))
recur(x)
