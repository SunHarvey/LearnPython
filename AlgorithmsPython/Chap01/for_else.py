import random

n = int(input("随机数的个数: "))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print("\n因特殊情况终止")
        break
else:
    print("\n随机数生成结束")
