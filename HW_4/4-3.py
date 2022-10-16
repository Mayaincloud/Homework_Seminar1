# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.
# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]


from random import randint 

n = int(input('Введите количество элементов списка: '))

def get_array(n):
    if n < 0:
        print("Negative value of the number of numbers!")
    my_array = []
    for i in range(n):
        my_array.append(randint(0, 9))
    return my_array


def get_chandge_array(my_array: list):
    new_array = []
    
    for i in range(len(my_array)):
        if my_array.count(my_array[i]) == 1:
            new_array.append(my_array[i])
    return new_array         


my_array = get_array (n)
print(my_array)
new_array = get_chandge_array(my_array)
print(new_array)