# 1. Задайте список, состоящий из произвольных чисел, количество задаёт 
# пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном 
# списке число,
#    полученное от пользователя.

from random import sample

def find_number(count, number):
    count = count if count > 0 else -count
    array = sample(range(1, count * 2), count)
    print(array)
    if number in array:
        return True
    return False

print(find_number(10, 5))