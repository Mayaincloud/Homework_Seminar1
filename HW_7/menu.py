import search
import exceptions
import log

def menu():
    while True:
        print('1. Показать весь справочник')
        print('2. Поиск записи по имени/фамилии/номеру телефона')
        print('3. Добавить запись в справочник')
        print('4. Изменить запись в справочнике')
        print('5. Удалить запись из справочника')
        print('6. Выход\n')
        print('Выберите вид операции')
        operation = exceptions.type_of_number()

        if operation == 1:
            log.logging.info('Selected item number 1')
            search.read()

        elif operation == 2:
            log.logging.info('Selected item number 2')
            my_search = search.search()
            log.logging.info(f'User entered: {my_search}')

        elif operation == 3:
            log.logging.info('Selected item number 3')
            my_add = search.add()
            log.logging.info(f'User entered: {my_add}')

        elif operation == 4:
            log.logging.info('Selected item number 4')
            my_change = search.change()
            log.logging.info(f'User entered: {my_change}')

        elif operation == 5:
            log.logging.info('Selected item number 5')
            my_delete = search.delete()
            log.logging.info(f'User entered: {my_delete}')
        
        elif operation == 6:
            log.logging.info('End')
            break

        else:
            print('Такой операции нет в списке, попробуйте еще раз')
