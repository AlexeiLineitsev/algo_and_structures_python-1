"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

n = int(input('n = '))

summ_left = 0
summ_right = 0

for i in range(1,n+1):
    summ_left = summ_left + i

summ_right = n * (n+1)/2

print(summ_left, ' = ',summ_right)

