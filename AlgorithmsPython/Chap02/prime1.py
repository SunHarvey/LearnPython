count = 0

for n in range(2, 1000):
    for i in range(2, n):
        count += 1
        if n % i == 0:
            break
    else:
        print(n)

