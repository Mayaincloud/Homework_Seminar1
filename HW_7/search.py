from dataclasses import replace


def read():
    with open ('contacts.csv', 'r', encoding = 'utf-8') as my_f:
        tel_dir = my_f.readlines()
        for line in tel_dir:
            print(line.strip())
        print()

def search():
    with open('contacts.csv', 'r', encoding = 'utf-8') as my_f1:
        tel_dir = my_f1.readlines()
        flag = 1
        name = input('Введите имя или фамилию, или номер телефона\n')
        for line in tel_dir:       
            if name in line:
                flag = 0
                print(line)
        if flag: print('Данные не найдены')
    return name

def add():
    with open('contacts.csv', 'a', encoding = 'utf-8') as my_f2:
        line = input('Введите через пробел Имя Фамилия Номер_телефона\n')
        my_f2.write(line + '\n')
    return line

def change():
    with open('contacts.csv', 'r', encoding = 'utf-8') as my_f3:
        tel_dir = my_f3.readlines()
        flag = 1
        name = input('Номер телефона записи, которую хотите изменить\n')
        with open('contacts.csv', 'w', encoding = 'utf-8') as my_f:
            for line in tel_dir:       
                if name in line:
                    flag = 0
                    print(line)
                    new_line = input('Введите через пробел Имя Фамилия Номер_телефона\n')
                    my_f.write(new_line + '\n')
                else:
                    my_f.write(line)
            if flag: print('Данные не найдены')
    return name, new_line

def delete():
     with open('contacts.csv', 'r', encoding = 'utf-8') as my_f3:
        tel_dir = my_f3.readlines()
        flag = 1
        name = input('Номер телефона записи, которую хотите удалить\n')
        with open('contacts.csv', 'w', encoding = 'utf-8') as my_f:
            for line in tel_dir:       
                if name not in line:
                    my_f.write(line)
            if flag: print('Данные не найдены')
        return name

