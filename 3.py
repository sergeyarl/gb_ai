#!/usr/bin/env python


# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

in_num = int(input('Введите натуральное число: '))
res_num = ''

while in_num != 0:
    l_dig = in_num % 10
    res_num = f'{res_num}{l_dig}'
    in_num = int(float(in_num / 10))

print(res_num)
