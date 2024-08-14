print("输出*")
n = int(input("符号总数:"))
w = int(input("每隔多少个换行:"))

for _ in range(n // w):
    print("*" * w)

reset = n % w
if reset:
    print('*' * reset)
