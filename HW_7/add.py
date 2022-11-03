from dataclasses import replace

def add():
    with open('C:\\Users\\User\\Desktop\\git education\\Py_class\\HW_7\\contacts.csv', 'a', encoding = 'utf-8') as my_f:
        line = input('Введите через пробел Имя Фамилия Номер_телефона\n')
        my_f.write(line)
        my_f.write('\n')
    
