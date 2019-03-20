# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.


def summa_row(a, digit):
    summ = 0
    for i in a:
        if i % digit == 0:
            summ = summ + 1
    return summ



a = [i for i in range(2,100)]
b = [i for i in range(2,10)]


for i in b:
    print('Числу', i,' в диапазоне натуральных чисел от 2 до 99 кратны ',summa_row(a,i), 'чисел')
