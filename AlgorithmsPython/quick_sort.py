# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [j for j in array[1:] if j > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)
#
# print(quick_sort(ls))

# def quick_sort2(array):
#     if len(array) <= 1:
#         return array
# else:
#     pivot = array[len(array) // 2]
#     less = []
#     middle = []
#     greater = []
#     for i in array:
#         if i < pivot:
#             less.append(i)
#         elif i > pivot:
#             greater.append(i)
#         elif i == pivot:
#             middle.append(i)
# return quick_sort2(less) + middle + quick_sort2(greater)


# ls = [1, 5, 10, 8, 9, 10, 11, 7]
# print(quick_sort2(ls))
