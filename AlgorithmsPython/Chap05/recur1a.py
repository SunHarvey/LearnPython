def recur(n: int):
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2


x = int(input("请输入一个整数: "))
recur(x)
