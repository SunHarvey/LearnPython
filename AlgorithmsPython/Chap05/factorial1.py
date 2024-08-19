def factorial(n: int) -> int:
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


if __name__ == '__main__':
    number = int(input("Enter a number: "))
    print(f"{number}的阶乘为: {factorial(number)}")
