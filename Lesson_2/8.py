"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""
def summ_digits(n,digit,summ):
    if n != 0:
        number = int(input('Введите число - '))
        summ = summ + decomposition_number(number,digit)
        return summ_digits(n-1,digit,summ)
    elif n == 0:
        return summ



def decomposition_number(number,digit):
    summ = 0
    while number != 0:
        digit_current = number % 10
        number = int(number / 10)
        if digit == digit_current:
            summ = summ + 1
    return summ






n = int(input('Количество чисел - '))
digit = int(input('Цифра которую считаем - '))
summ = 0

print(summ_digits(n,digit,summ))
