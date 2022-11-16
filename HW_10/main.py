import telebot
from telebot import types

import modul_sum as sum
import modul_sub as sub
import modul_mult as mult
import modul_power as pow
import modul_div as div
import exceptions
import log



bot = telebot.TeleBot("5723809096:AAHWVjbPmAiROfW3AFMEuJUgm-COI-Ot_uE")


@bot.message_handler(commands=['start'])
def start(message):
    log.logging.info('Start bot')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(f'/рациональные')
    button2 = types.KeyboardButton(f'/комплексные')
    markup.add(button1, button2)
    send_msg = f'Привет ✌️, {message.from_user.first_name}. Я - "бот-калькулятор!" Какие числа будем считать?'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['рациональные'])
def ration(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ рациональные')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton(f'/сложение')
    button2 = types.KeyboardButton(f'/вычитание')
    button3 = types.KeyboardButton(f'/умножение')
    button4 = types.KeyboardButton(f'/деление')
    button5 = types.KeyboardButton(f'/возведение_в_степень')
    button6 = types.KeyboardButton(f'/извлечение_квадратного_корня')
    markup.add(button1, button2, button3, button4, button5, button6)
    send_msg = f'Выбери операцию:'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['комплексные'])
def ration(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ рациональные')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton(f'/сумма')
    button2 = types.KeyboardButton(f'/разность')
    button3 = types.KeyboardButton(f'/произведение')
    button4 = types.KeyboardButton(f'/частное')
    button5 = types.KeyboardButton(f'/степень')
    button6 = types.KeyboardButton(f'/корень_квадратный')
    markup.add(button1, button2, button3, button4, button5, button6)
    send_msg = f'Выбери действие:'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['сложение'])
def action(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ сложение')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['вычитание'])
def action(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ вычитание')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['умножение'])
def action(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ умножение')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['деление'])
def action(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ деление')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)


@bot.message_handler(commands=['возведение_в_степень'])
def action(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ возведение_в_степень')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 2 числа через пробел. Для вещественных чисел разделитель точка (3.5)'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['извлечение_квадратного_корня'])
def action(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ извлечение_квадратного_корня')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи 1 число'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['сумма'])
def action(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ сумма')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи через пробел 4 числа: действительную затем мнимую части 1-го числа, потом второго.'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['разность'])
def action(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ разность')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи через пробел 4 числа: действительную затем мнимую части 1-го числа, потом второго.'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['произведение'])
def action(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ произведение')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи через пробел 4 числа: действительную затем мнимую части 1-го числа, потом второго.'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['частное'])
def action(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ частное')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи через пробел 4 числа: действительную затем мнимую части 1-го числа, потом второго.'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['степень'])
def action(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ степень')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи через пробел 3 числа: действительную затем мнимую части 1-го числа, потом степень.'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)

@bot.message_handler(commands=['корень_квадратный'])
def action(message):
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ корень_квадратный')
    global operation
    operation = message.text.split()
    markup = types.ForceReply(selective=True)
    send_msg = f'Введи через пробел 2 числа: действительную затем мнимую части комплексного числа.'
    bot.send_message(message.chat.id, send_msg, reply_markup=markup)



@bot.message_handler(content_types=['text'])
def exeption(message):
    get_msg_bot = message.text.split()
    log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ numbers = {get_msg_bot}')
    if operation == ['/сложение']:
        a, b = exceptions.numbers(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Ошибка!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = sum.sum(a, b)
            send_msg = f'{a} + {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        log.logging.info('End bot')

    elif operation == ['/вычитание']:
        a, b = exceptions.numbers(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Ошибка!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = sub.sub(a, b)
            send_msg = f'{a} - {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        log.logging.info('End bot')

    elif operation == ['/умножение']:
        a, b = exceptions.numbers(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Ошибка!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = mult.mult(a, b)
            send_msg = f'{a} * {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        log.logging.info('End bot')

    elif operation == ['/деление']:
        a, b = exceptions.numbers(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Ошибка!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = div.div(a, b)
            send_msg = f'{a} / {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        log.logging.info('End bot')

    elif operation == ['/возведение_в_степень']:
        a, b = exceptions.numbers(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Ошибка!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = pow.power(a, b)
            send_msg = f'{a} ** {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        log.logging.info('End bot')
    
    elif operation == ['/извлечение_квадратного_корня']:
        a = exceptions.square_root(get_msg_bot)
        print(a)
        if a == 0:
            send_msg = 'Ошибка!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = pow.power(a, 0.5)
            send_msg = f'{a} ** 0.5 = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        log.logging.info('End bot')

        
    elif operation == ['/сумма']:
        a, b = exceptions.complex_num(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Ошибка!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = sum.sum(a, b)
            send_msg = f'{a} + {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        log.logging.info('End bot')

    elif operation == ['/разность']:
        a, b = exceptions.complex_num(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Ошибка!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = sub.sub(a, b)
            send_msg = f'{a} - {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        log.logging.info('End bot')

    elif operation == ['/произведение']:
        a, b = exceptions.complex_num(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Ошибка!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = mult.mult(a, b)
            send_msg = f'{a} * {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        log.logging.info('End bot')

    elif operation == ['/частное']:
        a, b = exceptions.complex_num(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Ошибка!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = div.div(a, b)
            send_msg = f'{a} / {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        log.logging.info('End bot')

    elif operation == ['/степень']:
        a, b = exceptions.complex_pow(get_msg_bot)
        if a == 0 and b == 0:
            send_msg = 'Ошибка!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = pow.power(a, b)
            send_msg = f'{a} ** {b} = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        log.logging.info('End bot')

    elif operation == ['/корень_квадратный']:
        a = exceptions.complex_square(get_msg_bot)
        if a == 0:
            send_msg = 'Ошибка!'
            bot.send_message(message.chat.id, send_msg)
            log_result = 'error'
        else:
            result = pow.power(a, 0.5)
            send_msg = f'{a} ** 0.5 = {result}'
            log_result = f'{result}'
            bot.send_message(message.chat.id, send_msg)
        log.logging.info(f'{message.from_user.first_name}/ {message.from_user.id}/ result = {log_result}')
        log.logging.info('End bot')
    
   

    send_msg = f'Начать новое вычисление /start'
    bot.send_message(message.chat.id, send_msg)

bot.polling(non_stop=True)