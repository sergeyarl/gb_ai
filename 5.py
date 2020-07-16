#!/usr/bin/evn python

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random
from pprint import pprint

size = 10
min_item = -100
max_item = 100

array = [random.randint(min_item, max_item) for _ in range(size)]

pprint(array)

biggest_neg_num = min_item
biggest_neg_num_pos = 0

i = 0

for element in array:
    if element < 0 and element > biggest_neg_num - 1:
        biggest_neg_num = element
        biggest_neg_num_pos = i

    i += 1

print(f'Максимальный отрицательный элемент: {biggest_neg_num}')
print(f'Позиция в списке: {biggest_neg_num_pos}')
