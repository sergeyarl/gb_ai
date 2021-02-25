#!/usr/bin/env python

# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
# https://drive.google.com/file/d/12SJIEQK46zqudzTxGj2DmYO44byc-8Ai/view?usp=sharing

input_year = input('Введите год: ')

result = int(input_year) / 4

if result.is_integer():
    print("Год високосный.")
else:
    print("Год не високосный")
