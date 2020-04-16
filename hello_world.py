#9
def reverse_list(lst):
    half_len = int(len(lst) / 2)
    for i in range(half_len):
        lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst

print(reverse_list([37, 2, 1, -9]))
print(reverse_list([37, 2, 1, -9, 5]))
print(reverse_list([]))
print(reverse_list([1]))
print(reverse_list([1, 2]))

    