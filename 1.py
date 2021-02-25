#!/usr/bin/env python

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1uZRuXwjQHWECNZJHM_lHh-JjgkBmclqF/view?usp=sharing

number = input('Ввдите трехзначное число: ')

sum = int(number[0]) + int(number[1]) + int(number[2])
prod = int(number[0]) * int(number[1]) * int(number[2])

print(f'сумма цифр введенного числа: {sum}')
print(f'произведение цифр вве55денного числа: {prod}')