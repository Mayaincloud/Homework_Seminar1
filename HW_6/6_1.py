# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint

n = int(input('Введите количество элементов списка: '))

if n < 0:
    print("Negative value of the number of numbers!")
else:
    arr = [randint(0, 9) for i in range(n)]
    print (arr)

new_arr = [arr[i+1] for i in range (len(arr) -1) if arr[i] < arr[i+1]] 
print (new_arr)
