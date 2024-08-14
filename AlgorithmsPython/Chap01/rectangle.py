area = int(input("请输入矩形面积:"))
for i in range(1, area):
    if i * i > area:
        break
    if area % i:
        continue
    # else:
    print("%s x %s" % (i, int(area / i)))
