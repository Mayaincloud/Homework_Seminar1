# 1. В файле находится N натуральных чисел, записанных через пробел.
#    Среди чисел не хватает одного, чтобы выполнялось условие
#    A[i] - 1 = A[i-1]. Найдите это число.

import random

def getArr():
    path='Lesson_5/5_1.txt'
    data = open(path, 'r')
    arr = list(map(int, (data.readline().split(' '))))
    data.close()
    arr.remove(random.choice(arr))
    print(arr)
    return arr

def checkArr2(arr):
    if arr[0] == 0:
       return 0
    for i in range(1, len(arr)):
        if (arr[i]-1) != arr[i-1]:
            return (arr[i]) - 1
    return -1

print(checkArr2(getArr()))
