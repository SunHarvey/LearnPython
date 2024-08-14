print("-" * 27)

for i in range(1, 10):
    for j in range(1, 10):
        print("{}*{}={}".format(j, i, i * j), end=" ")
        if i == j:
            print()
            break
print("-" * 27)
