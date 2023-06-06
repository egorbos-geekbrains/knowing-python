import os
import sys
import telebot

# Вспомогательные функции
def write_question_to_file(filename: str, user_id: str, question: str):
    with open(filename, 'a', encoding="utf-8") as file:
        file.write('%s:%s\n' % (user_id, question))

print('\nЗадача № 1')
token = sys.argv[1] if len(sys.argv) == 2 else os.environ['BOT_TOKEN'] if 'BOT_TOKEN' in os.environ else None

if token == None:
    print('Ошибка: не указан token!')
    sys.exit()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_chat(message):
    bot.send_message(
        message.chat.id,
        f'Привет, {message.from_user.first_name}!\nЗадай свой вопрос в сообщении, и мы в ближайшее время обязательно на него ответим!'
        )

@bot.message_handler(content_types=['text'])
def receive_question(message):
    write_question_to_file('questions.txt', message.from_user.id, message.text)
    bot.send_message(message.chat.id, 'Я записал вопрос, ожидайте ответ от оператора!')

print('Бот запущен...')
bot.infinity_polling()