# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4

# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5

# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import randint

n = int(input('Введите количество элементов списка: '))

def get_array(n):
    array = []
    for i in range(n):
        array.append(randint(0, 9))
    return array

def product_items(array):
    result = []
    if len(array) % 2 == 0: 
        length = len(array)//2
    else:
        length = len(array)//2 + 1
    for i in range(0, length): 
        if i != len(array) - i - 1:
            product = array[i] * array[len(array) - i - 1]
        else:
            product = array[i]
        result.append(product)
    return result

new_array = get_array(n)
print(new_array)
print(product_items(new_array))