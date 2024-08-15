import random
from max import max_of

print("求随机数的最大值")
num = int(input("随机数个数:"))
lo = int(input("随机数下限:"))
hi = int(input("随机数上限:"))
x = [None] * num

for i in range(num):
    x[i] = random.randint(lo, hi)

print(x)
print("最大值为{}".format(max_of(x)))
