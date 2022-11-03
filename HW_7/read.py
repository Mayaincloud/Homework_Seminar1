def read():
    with open ('C:\\Users\\User\\Desktop\\git education\\Py_class\\HW_7\\contacts.csv', 'r', encoding = 'utf-8') as my_f:
        tel_dir = my_f.readlines()
        for line in tel_dir:
            print(line.strip())
        print()

