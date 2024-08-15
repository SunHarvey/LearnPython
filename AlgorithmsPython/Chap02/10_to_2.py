def reverse_10_to_2(n):
    bin_number = []
    int_part, remainder = divmod(n, 2)
    bin_number.append(1)
    while int_part != 0:
        bin_number.append(remainder)
        int_part, remainder = divmod(int_part, 2)
        print(int_part)

    print(bin_number)


number = 1
reverse_10_to_2(number)
