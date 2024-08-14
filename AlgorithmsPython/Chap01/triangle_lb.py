print("请输入左下角的等腰三角形")
n = int(input("短边长度:"))

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
