# 1. Напишите программу, которая принимает на вход число N и 
# выдаёт последовательность из N членов.


# N = int(input('Введите N: '))
# result = 1
# for i in range(N):
#     result = result * -3
#     print(result, end = ' ')

N = int(input('Введите N: '))
for i in range(N):
    #print((-3)**i)
    print(3**i*(-1)**i)