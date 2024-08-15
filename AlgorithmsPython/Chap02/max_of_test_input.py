from max import max_of

print("求数组的最大值")
print("备注:收到End后结束输入")

number = 0
x = []

while True:
    s = input("x[{}]:".format(number))
    if s == "End":
        break
    x.append(int(s))
    number += 1

print("已读取{}个元素".format(number))
print("最大值为{}".format(max_of(x)))
