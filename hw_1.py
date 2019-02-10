#!/usr/bin/env python

# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

s_str = "ccaabaabcccaa"

s_str_hash = hash(s_str)

# можно выполнить просто через set.
#
# subs = set()
# 
# for i in range(len(s_str)):
#     for n in range(i, len(s_str)):
#         if hash(s_str[i:n + 1]) != s_str_hash:
#             subs.add(s_str[i:n + 1])
# 
# for i in subs:
#     print(i)
# 

# а можно сложно через list и хеш суммы
#
subs = []

for i in range(len(s_str)):
    for n in range(i, len(s_str)):
        aaa = 0
        for e in subs:
            if hash(s_str[i:n + 1]) == hash(e):
                aaa = 1
                break

        if aaa == 1:
            continue

        if hash(s_str[i:n + 1]) != s_str_hash:
            subs.append(s_str[i:n + 1])

# но думаю наверняка можно сделать еще проще и при этом по условию задания.
# сорри, если намудрил.

for i in subs:
    print(i)


