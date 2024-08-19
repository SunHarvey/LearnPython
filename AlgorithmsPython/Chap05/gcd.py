def gcd(x: int, y: int) -> int:
    """求整数x和y的最大公约数并返回"""
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


if __name__ == '__main__':
    print(gcd.__doc__)
    x = int(input("整数1:"))
    y = int(input("整数2:"))
    print(f"最大公约数为{gcd(x, y)}")
