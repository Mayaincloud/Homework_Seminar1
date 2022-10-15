# 1. Задайте список, состоящий из произвольных чисел, 
# количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).
# in
# 5

# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4

# out
# [4, 2, 4, 9]
# 8


from random import randint

n = int(input('Введите количество элементов списка: '))

def get_array(n):
    array = []
    for i in range(n):
        array.append(randint(0, 9))
    return array

def sum_elements_array(array):
    sum = 0
    for i in range(0, len(array), 2): 
        sum = sum + array[i]
    return sum

new_array = get_array(n)
print(new_array)
print(sum_elements_array(new_array))