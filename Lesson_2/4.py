"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

def row_n(n, elem, summ):
    while n != 0:
        summ = summ + elem
        elem = elem / -2
        n = n - 1
        return row_n(n, elem, summ)
    return summ




n = int(input('n = '))
elem = 1
summ = 0

print('Cумма n элементов следующего ряда чисел(1 -0.5 0.25 -0.125 ...)=', row_n(n, elem, summ))


