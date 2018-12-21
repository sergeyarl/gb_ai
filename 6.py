#!/usr/bin/env python

# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его
# отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться
# больше или меньше введенное пользователем число, чем то, что загадано. Если за 10
# попыток число не отгадано, то вывести загаданное число.

from random import randint


def check_guess(secret_num, attempt=1):
    max_attempts = 10

    if attempt <= max_attempts:
        guess_num = int(input('Введите целое число от 0 до 100: '))

        if guess_num != secret_num:
            if guess_num < secret_num:
                print('Введенное число меньше загаданного.')
            elif guess_num > secret_num:
                print('Введенное число больше загаданного.')

            attempt += 1
            check_guess(secret_num, attempt)
        else:
            print('Вы угадали число!')
            exit(0)
    else:
        print('Вы исчерпали максимальное количество попыток!')
        print(f'Загаданное число: {secret_num}')
        exit(0)


check_guess(randint(0, 100))
