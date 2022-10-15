# 3. Напишите программу, которая будет преобразовывать десятичное число 
# в двоичное.
# Без использования встроенной функции преобразования, без строк.

# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

n = int(input('Введите число: '))

def conversion_to_binary(number):
    result = []
    while number > 0: 
        remains = number % 2
        number = number // 2
        result.append(remains)
 
    result.reverse()
    return result

binary_number = conversion_to_binary(n)
for i in range(len(binary_number)):
    print(binary_number[i], end = '')