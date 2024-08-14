print("直角右下角等腰三角形")
n = int(input("短边长度:"))

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
