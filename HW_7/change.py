
def change():
    with open('C:\\Users\\User\\Desktop\\git education\\Py_class\\HW_7\\contacts.csv', 'r', encoding = 'utf-8') as my_f:
        tel_dir = my_f.readlines()
        flag = 1
        name = input('Номер телефона записи, которую хотите изменить\n')
        with open('C:\\Users\\User\\Desktop\\git education\\Py_class\\HW_7\\contacts.csv', 'w', encoding = 'utf-8') as my_f:
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
