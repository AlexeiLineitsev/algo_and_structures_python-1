"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
import collections

count_company = int(input('Желаемое количество компаний - '))

companys = collections.defaultdict(list)

s = 0

for i in range(count_company):

    name_company = input('Имя компании - ')
    profit_company = [int(input('Введите прибыль за {} квартал - '.format(j+1))) for j in range(4)]
    companys[name_company] = sum(profit_company)
    s += sum(profit_company)

s = s / count_company
print('Cредняя прибыль (за год для всех предприятий) = ', round(s,0 ))

print('Прибыль выше среднего')
for i in companys:
    if companys[i] > s:
        print(i)

print('Прибыль ниже среднего')
for i in companys:
    if companys[i] < s:
        print(i)




