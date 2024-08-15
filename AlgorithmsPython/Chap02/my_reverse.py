def my_reverse(array):
    n = len(array)
    for i in range(n // 2):
        array[i], array[n - 1 - i] = array[n - 1 - i], array[i]
    print(array)


ls = [1, 2, 3, 4, 5, 6, 7]
my_reverse(ls)
