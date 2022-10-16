# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# in
# 54

# out
# [2, 3, 3, 3]

# in
# 9990

# out
# [2, 3, 3, 3, 5, 37]

# in
# 650

# out
# [2, 5, 5, 13]

n = int(input('Введите число: '))

def get_prime_factors(n):
    i = 2
    result = []
    while i**2 <= n:
        while n % i == 0:
            result.append(i)
            n = n / i
        i += 1
    if n > 1:
        result.append(int(n))
    return result



print(get_prime_factors(n))