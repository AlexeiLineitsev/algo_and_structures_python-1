"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

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

a = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9]

max_index = find_max_or_min_in_list(a,1)
min_index = find_max_or_min_in_list(a,0)

summ = 0

for i in range(min_index + 1, max_index):
    summ = summ + a[i]

print('Сумма элементов, за исключением максимально и минимального ',summ)