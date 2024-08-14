print("求1和n之间所有整数之和")

while True:
    n = int(input("n的值:"))
    if n>0:
        break
    else:
        print("请输入的n大于0")
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)
