def search():
    with open('C:\\Users\\User\\Desktop\\git education\\Py_class\\HW_7\\contacts.csv', 'r', encoding = 'utf-8') as my_f:
        tel_dir = my_f.readlines()
        flag = 1
        name = input('Введите имя или фамилию, или номер телефона\n')
        for line in tel_dir:       
            if name in line:
                flag = 0
                print(line)
        if flag: print('Данные не найдены')
    return name
