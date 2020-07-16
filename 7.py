#!/usr/bin/env python

# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random
from pprint import pprint

size = 10
min_item = 1
max_item = 10

array = [random.randint(min_item, max_item) for _ in range(size)]

pprint(array)

min_num_1 = max_item
min_num_1_pos = 0
min_num_2 = max_item

# возможно не очень хорошее решение с двойным перебором массивов.
# но на другое у меня к сожалению не хватило времени.

i = 0
for element in array:
    if element < min_num_1:
        min_num_1 = element
        min_num_1_pos = i

    i += 1

i = 0
for element in array:
    if element < min_num_2 and i != min_num_1_pos:
        min_num_2 = element
        min_num_2_pos = i

    i += 1

print(f'{min_num_1}, {min_num_2}')
