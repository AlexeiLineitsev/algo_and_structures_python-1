"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

def even(number):
    s = ''
    sum = 0
    while number != 0:
        digit = number % 10
        number = int(number / 10)
        if digit % 2 == 0:
            s = ' ' + str(digit) + ' ' + s
            sum += 1

    return 'Четных {}({})'.format(sum,s)

def odd(number):
    s = ''
    sum = 0
    while number != 0:
        digit = number % 10
        number = int(number / 10)
        if digit % 2 != 0:
            s = ' ' + str(digit) + ' ' + s
            sum += 1

    return 'Нетных {}({})'.format(sum,s)

number = int(input('Ваше число = '))
print(even(number))
print(odd(number))
