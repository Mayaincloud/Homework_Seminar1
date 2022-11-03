
def delete():
     with open('C:\\Users\\User\\Desktop\\git education\\Py_class\\HW_7\\contacts.csv', 'r', encoding = 'utf-8') as my_f:
        tel_dir = my_f.readlines()
        flag = 1
        name = input('Номер телефона записи, которую хотите удалить\n')
        with open('C:\\Users\\User\\Desktop\\git education\\Py_class\\HW_7\\contacts.csv', 'w', encoding = 'utf-8') as c:
            for line in tel_dir:       
                if name not in line:
                    c.write(line)
            if flag: print('Данные не найдены')
        return name


