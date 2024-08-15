t1 = 1,
print(t1, type(t1))

t2 = (1, 2, [3, 4])
print(t2, id(t2), type(t2))
t2[2].append(5)
print(t2, id(t2), type(t2))
