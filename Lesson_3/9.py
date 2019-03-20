# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

N = 5
M = 4

a = [[-1, 5, 7, 13], [5, 4, 7, 16], [1, 4, 5, 10], [7, 4, 6, 17], [9, 6, 5, 20]]

# for i in range(N):
#     b = []
#     b = input('Введите элементы матрицы, 3 числа через пробел  ').split()
#     b = [int(i) for i in b]
#     b.append(sum(b))
#     a.append(b)

for i in range(N):
    for j in range(M):
        print(a[i][j], end='  ')
    print()

for i in range(M):
    print('--', end=' ')

print()

max = 0

for j in range(M):
    min = a[0][j]
    for i in range(N):
        if min > a[i][j]:
            min = a[i][j]
            if max < min:
                max = min
    max = min
    print(min, end='  ')

print()
print('Максимальный элемент среди минимальных элементов столбцов матрицы',max)
