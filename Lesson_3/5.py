#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

def find_min_in_list(a):
    min_a = a[0]
    for i in range(len(a)):
        if min_a > a[i]:
            min_a = a[i]
            index = i
    return index

a = [-1, -2 , -3, -4, 1, 2, 3, 4]
b = find_min_in_list(a)
print('Максимально отрицательный элемент ', a[b], 'его индекс ', b)