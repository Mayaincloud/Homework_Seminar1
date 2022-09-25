a = int(input('a = '))
if((a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0):
    print('true')
else:
    print('false')