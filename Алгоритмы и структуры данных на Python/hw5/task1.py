#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
#Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
#чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import deque

n = int(input('Введите кол-во предприятий: '))
d = deque(maxlen=4)
QR = 4
a = {}

for i in range(n):
    name = input(f'Название предприятия №{i + 1}: ')
    summ_ = 0
    for j in range(QR):
        k = int(input(f'Прибыль за {j + 1}-й квартал: '))
        d.append(k)
    summ_ = sum(d)
    a[name] = summ_

average = sum(a.values()) / len(a)

print('Предприятия с прибылью выше среднего: ')
for k in a:
    if a[k] > average:
        print(k)

print('Предприятия с прибылью меньше среднего: ')
for h in a:
    if a[h] < average:
        print(h)
