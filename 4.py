#!/usr/bin/evn python

# 4. Определить, какое число в массиве встречается чаще всего.

import random
from pprint import pprint

size = 100
min_item = 1
max_item = 10

array = [random.randint(min_item, max_item) for _ in range(size)]
pprint(array)

max_occ = None
max_occ_num = 0

for x in range(min_item, max_item + 1):
    i = 0

    for el in array:
        if el == x:
            i += 1

    if i > max_occ_num:
        max_occ = x
        max_occ_num = i

print(f'Число {max_occ} встречается в массиве чаще всего ({max_occ_num} раз).')
