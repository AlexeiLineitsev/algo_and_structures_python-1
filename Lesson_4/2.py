"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

n = int(input('Число = '))
a = []

for i in range(n + 1):
    a.append(i)

a[1] = 0


# Без использования «Решета Эратосфена»
i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1
a = set(a)
a.remove(0)
print(a)



# алгоритм «Решето Эратосфена»
def list_a(a, i):
    p = a[i]
    try:
        while i <= n:
            a[i * p] = 0
            i += 1
    except:
        pass
    return a

i =2
while i <= n:
    if a[i] != 0:
        list_a(a, i)
    i += 1

a = sorted(set(a))
a.remove(0)
# print(a)

