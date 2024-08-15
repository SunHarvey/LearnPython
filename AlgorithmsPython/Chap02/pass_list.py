def change(lst, idx, val):
    """将lst[idx]的值修改为val"""
    lst[idx] = val


x = [11, 22, 33, 44, 55]
print('x=', x)

index = int(input("下标:"))
value = int(input("新值:"))

change(x, index, value)
print("x = {}".format(x))
