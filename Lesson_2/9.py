"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
def summa_number(number):
    summ = 0
    while number != 0:
        digit_current = number % 10
        number = int(number / 10)
        summ = summ + digit_current
    return summ


def search_max_summ_digits(n, previous_summ,number_current):
    if n != 0:
        number = int(input('Введите число - '))
        summ = summa_number(number)
        if summ > previous_summ:
            max_summ = summ
            number_current = number
        return search_max_summ_digits(n-1, max_summ,number_current)
    else:
        return 'Наибольшее по сумме число {} его сумма равна {}'.format(number_current,previous_summ)



n = int(input('Количество чисел - '))
previous_summ = 0


print(search_max_summ_digits(n,previous_summ,0))
