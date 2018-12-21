#!/usr/bin/env python

# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

in_num = int(input('Введите натуральное число: '))

odds_num = 0
evens_num = 0

while in_num != 0:

    if float(in_num / 2).is_integer():
        evens_num += 1
    else:
        odds_num += 1

    in_num = int(in_num / 10)

print(f'Количество нечетных цифр: {odds_num}')
print(f'Количество четных цифр: {evens_num}')
