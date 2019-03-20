#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

def find_max_or_min_in_list(a, key):
    max_a = a[0]
    min_a = a[0]
    index = 0
    if key == 1:
        for i in range(len(a)):
            if max_a < a[i]:
                max_a = a[i]
                index = i
        return index
    else:
        for i in range(len(a)):
            if min_a > a[i]:
                min_a = a[i]
                index = i
        return index


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]


a [find_max_or_min_in_list(a, 1)], a[find_max_or_min_in_list(a, 0)] = a[find_max_or_min_in_list(a, 0)], a [find_max_or_min_in_list(a, 1)]


print(a)