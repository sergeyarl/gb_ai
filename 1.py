#!/usr/bin/env python

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю
# прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

# задача выполненна через namedtuple

from collections import namedtuple
from pprint import pprint
import sys
import types

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

all_vars = dict(vars())
for var_name, var in all_vars.items():
    if type(var) not in [types.ModuleType, types.FunctionType] and not var_name.startswith("_"):
        print(f'type = {type(var)}, size = {sys.getsizeof(var)}, var_name = {var_name}, object = {var}')


# OS: 64 bit
# Python 3.6.7 
#
# type = <class 'list'>, size = 96, var_name = ent_list, object = [Ent_t(name='ent1', q1='55', q2='44', q3='33', q4='22'), Ent_t(name='ent2', q1='99', q2='77', q3='22', q4='33')]
# type = <class 'int'>, size = 28, var_name = ent_number, object = 2
# type = <class 'type'>, size = 888, var_name = Ent_data, object = <class '__main__.Ent_t'>
# type = <class 'int'>, size = 28, var_name = i, object = 2
# type = <class '__main__.Ent_t'>, size = 88, var_name = lst, object = Ent_t(name='ent2', q1='99', q2='77', q3='22', q4='33')
# type = <class 'dict'>, size = 240, var_name = averages, object = {'ent1': 38.5, 'ent2': 57.75}
# type = <class 'float'>, size = 24, var_name = average_total, object = 48.125
# type = <class 'list'>, size = 96, var_name = h_av, object = ['ent2']
# type = <class 'list'>, size = 96, var_name = l_av, object = ['ent1']
# type = <class 'str'>, size = 53, var_name = key, object = ent2
