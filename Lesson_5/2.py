"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


import collections
import functools

number = collections.defaultdict(list)

for i in range(2):
    n = str(input('Ваше шестнадцатеричное число - '))
    number [i+1] = list(n)

print(number)

sum = sum([int(''.join(i), 16) for i in number.values()])

print('Сумма', sum)

sum = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in number.values()])

print('Произведение', sum)