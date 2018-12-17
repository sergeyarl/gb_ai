#!/usr/bin/env python

# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)
# https://drive.google.com/file/d/1POzyiREj7tD-hqhabNi5BO8CyP0kTNr2/view?usp=sharing


print('Введите 3 разных числа: ')
a = float(input('введите первое число: '))
b = float(input('введите втроое число: '))
c = float(input('введите третье число: '))

if a < b:
    if a < c:
        if b > c:
            print(f'среднее число: {c}')
        else:
            print(f'среднее число: {b}')
    else:
        print(f'среднее число: {a}')

else:
    if b < c:

        if a > c:
            print(f'среднее число: {c}')
        else:
            print(f'среднее число: {a}')
    else:
        print(f'среднее число: {b}')
