#!/usr/bin/env python

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random
from pprint import pprint

size = 10
min_item = 1
max_item = 10

array = [random.randint(min_item, max_item) for _ in range(size)]

pprint(array)

min_num = max_item
min_num_pos = 0
max_num = min_item
max_num_pos = 0

num_sum = 0

i = 0
for element in array:
    if element < min_num:
        min_num = element
        min_num_pos = i

    if element > max_num:
        max_num = element
        max_num_pos = i

    i += 1

print(f'min: {min_num} -> {min_num_pos}, max: {max_num} -> {max_num_pos}')

if max_num_pos > min_num_pos:
    for x in range(min_num_pos + 1, max_num_pos):
        num_sum += array[x]

elif max_num_pos < min_num_pos:
    for x in range(max_num_pos + 1, min_num_pos):
        num_sum += array[x]

print(f'Sum: {num_sum}')
