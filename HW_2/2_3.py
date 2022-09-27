# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и 
# выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = int(input('Введите число: '))
my_list = []
for k in range(1, n + 1):
    my_list.append(round((1 + 1/k) ** k))
sum = 0
for i in range(n):
    sum = sum + my_list[i]
print('Сумма чисел списка ', my_list, ' - ', sum)