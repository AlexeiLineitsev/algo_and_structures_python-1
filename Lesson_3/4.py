# 4.	Определить, какое число в массиве встречается чаще всего.

def number_list(a,index):
    summ = 0
    for i in a:
        if a[index] == i:
            summ += 1
    return summ


a = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 7, 8, 9]

max = 0

for i in range(len(a)):
    if max <= number_list(a,i):
        max = number_list(a,i)
        index = i


print('Число ', a[index], ' в массиве встречается чаще всего', max , 'раза')