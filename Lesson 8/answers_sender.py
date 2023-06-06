import os
import sys
import telebot

# Вспомогательные функции
def get_file_lines(filename: str):
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()
        return lines

def split_key_value(text: str):
    splitted = text.split(':')
    return (splitted[0], splitted[1].strip().rstrip('\n'))

def convert_lines_to_tuples_list(lines: list[str]):
    return [split_key_value(line) for line in lines]

def get_questions():
    questions_lines = get_file_lines("questions.txt")
    return convert_lines_to_tuples_list(questions_lines)

print('\nЗадача № 2')
token = sys.argv[1] if len(sys.argv) == 2 else os.environ['BOT_TOKEN'] if 'BOT_TOKEN' in os.environ else None

if token == None:
    print('Ошибка: не указан token!')
    sys.exit()

bot = telebot.TeleBot(token)

questions = get_questions()
for question in questions:
    print(f'\nВопрос: {question[1]}')
    bot.send_message(question[0], input('Ответ: '))