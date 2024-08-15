def card_conv(x: int, r: int) -> str:
    d = ''
    dchar = "01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while x > 0:
        d += dchar[x % r]
        x //= r
    return d[::-1]


if __name__ == '__main__':
    print("对十进制数进行转化")
    while True:
        while True:
            no = int(input("要转化对非负整数:"))
            if no > 0:
                break
        while True:
            cd = int(input("转化成二进制数(2-36): "))
            if 2 <= cd <= 36:
                break
        print("用{}进制数表示为{}".format(cd, card_conv(no, cd)))
        retry = input("是否再转化一次(y/n):")
        if retry in {"n", "N"}:
            break
