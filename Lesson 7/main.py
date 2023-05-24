import sys
import telebot
from random import randint
from typing import TypeVar
from collections.abc import Callable, Iterable

# Задача № 1
T = TypeVar('T')
R = TypeVar('R')
def map_to(func: Callable[[T], R], iterable: Iterable[T]):
    return list([func(e) for e in iterable])

# Задача № 2
def repeat_func(count: int):
    def test(func):
        def decorator():
            for _ in range(0, count):
                func()
        return decorator
    return test

print('Задача № 1')
numbers_list = [1, 2, 3, 4, 5]
print(f'Список: {numbers_list}')
numbers_list = map_to(lambda e: e * 10, numbers_list)
print(f'Результат (e: e * 10): {numbers_list}')

print('\nЗадача № 2')
@repeat_func(10)
def test_func(): print('Magic!', end=' ')
test_func()

# https://t.me/GuessRandomNumberBot
print('\nЗадача № 3')
if len(sys.argv) < 2:
    print('Ошибка: не указан token!')
    sys.exit()

numbers = {}
user_attempts = {}
bot = telebot.TeleBot(sys.argv[1])

def get_clue(number: int):
    rand = randint(1, 5)
    if rand == 1:
        hundred = int(number / 100)
        min = 1 if hundred == 0 else hundred * 100
        max = 1000 if hundred == 9 else (hundred + 1) * 100
        return f'Число находится в диапазоне [{min}, {max}].'
    elif rand == 2:
        clue_number = number + 50
        return f'Если к числу прибавить 50, то результат будет больше {clue_number - 15}, но меньше {clue_number + 15}.'
    elif rand == 3:
        clue_number = number - 30
        return f'Если из числа вычесть 30, то результат будет больше {clue_number - 10}, но меньше {clue_number + 10}.'
    elif rand == 4:
        return f'Число больше {number - 5}.'
    elif rand == 5:
        return f'Число меньше {number + 5}.'

@bot.message_handler(commands=['start'])
def start_chat(message):
    user_attempts[message.from_user.id] = 0
    numbers[message.from_user.id] = randint(1, 1000)
    bot.send_message(
        message.chat.id,
        f'Привет, {message.from_user.first_name}!\nЯ загадал число от 1 до 1000, испытай свою удачу, попробуй отгадать!'
        )

@bot.message_handler(content_types=['text'])
def get_number(message):
    if not message.from_user.id in user_attempts:
        start_chat(message)
    else:
        try:
            user_attempts[message.from_user.id] += 1

            if int(message.text) == numbers[message.from_user.id]:
                bot.send_message(message.chat.id, f'Поздравляю! Угадано с {user_attempts[message.from_user.id]} попытки!')
                del numbers[message.from_user.id]
                del user_attempts[message.from_user.id]
            else:
                clue = get_clue(numbers[message.from_user.id])
                bot.send_message(message.chat.id, f'Неверно! {clue}')
        except ValueError:
            bot.send_message(message.chat.id, f'Ошибка в вводе числа! Будь повнимательнее!')

print('Бот запущен...')
bot.polling()