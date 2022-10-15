# 2. Задайте список, состоящий из произвольных слов, количество задаёт
# пользователь.
#    Напишите программу, которая определит индекс второго вхождения 
# строки в списке
#    либо сообщит, что её нет.

from random import choices

def set_of_random_words(length, word):
    array = []
    for i in range(length):
        result = choices(word, k = 3)
        array.append(''.join(result))
    return array

my_list = set_of_random_words(20, 'abc')
print(my_list)

def find_second_occurrence(word, array: list):
    if word in array and array.count(word) > 1:
        result = array.index(word)
        print(array.index(word, result + 1))
    else:
        print(-1)

find_second_occurrence(input('Введите слово: '), my_list)