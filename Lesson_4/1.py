"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import timeit
import cProfile


def summa_row(a, digit):
    summ = 0
    for i in a:
        if i % digit == 0:
            summ = summ + 1
    return summ



a = [i for i in range(2,100)]
b = [i for i in range(2,10)]
for i in b:
    print('Числу', i,' в диапазоне натуральных чисел от 2 до 99 кратны ',summa_row(a, i), 'чисел')

print()
print('Время выполнения 1000 раз - ',timeit.timeit('summa_row(a, i)', setup='from __main__ import summa_row, a, i', number=1000))
print()


def summa_row(a, digit):
    summ = 0
    for i in a:
        if i % digit == 0:
            summ = summ + 1
    return summ


def main():
    a = [i for i in range(2, 100)]
    b = [i for i in range(2, 10)]
    for i in b:
        print('Числу', i, ' в диапазоне натуральных чисел от 2 до 99 кратны ', summa_row(a, i), 'чисел')

if __name__ == '__main__':
    cProfile.run('main()')
