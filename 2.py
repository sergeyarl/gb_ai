#!/usr/bin/env python

# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
# значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в
# этих позициях первого массива стоят четные числа.

import random
from pprint import pprint

size = 10
min_item = 1
max_item = 10

array = [random.randint(min_item, max_item) for _ in range(size)]

pprint(array)

array_even = []

i = 0
for element in array:
    if element % 2 == 0:
        array_even.append(i)
    i += 1

pprint(array_even)



