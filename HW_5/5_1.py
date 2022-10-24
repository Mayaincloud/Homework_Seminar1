# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

import random

n = int(input('Введите количество слов: '))


def get_array(n):
    if n < 1:
        return print('введены некорректные данные')
    word = 'абв'
    arr = []
    for i in range(n):
        item = random.sample(word, k=3)
        arr.append(''.join(item))
    return arr


def new_array(arr):
    word = 'абв'
    filtered_str = ' '.join((filter(lambda i: i not in word, arr)))
    return filtered_str


print (get_array(n))
print (new_array(get_array(n)))