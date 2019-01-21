#!/usr/bin/env python

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю
# прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple
from pprint import pprint

ent_list = []
ent_number = int(input('Введите количество предприятий: '))

Ent_data = namedtuple('Ent_t', ['name', 'q1', 'q2', 'q3', 'q4'])

print('Введите через запятую без пробелов данные предприятий: наименование, прибыль за 1 кв, за 2кв, за 3кв, за 4кв')

for i in range(1, ent_number + 1):
    lst = Ent_data(*input(f'Предприятие {i}: ').split(','))
    ent_list.append(lst)

averages = { x.name: (float(x.q1) + float(x.q2) + float(x.q3) + float(x.q4))/4 for x in ent_list }
average_total = sum(averages.values()) / len(averages.values())

h_av = []
l_av = []

for key in averages:
    if averages[key] > average_total:
        h_av.append(key)
    elif averages[key] < average_total:
        l_av.append(key)

print(f'Средняя прибыль по всем предприятиям за год: {average_total}')
print(f'Предприятия, чья годовая прибыль выше среднего:')
pprint(h_av)
print(f'Предприятия, чья годовая прибыль ниже среднего:')
pprint(l_av)

