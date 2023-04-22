from random import randint

# Вспомогательные функции
def get_file_lines(filename: str):
    with open(filename, encoding="utf-8") as file:
        lines = file.readlines()
        return lines

def split_key_value(text: str, values_splitter: str = ','):
    splitted = text.split(':')
    return (splitted[0], splitted[1].strip().rstrip('\n').split(values_splitter))

def convert_lines_to_dict(lines: list[str], values_splitter: str = ','):
    pairs = [split_key_value(line, values_splitter) for line in lines]
    return dict(pairs)

def write_dict_to_file(filename: str, dict: dict, values_splitter: str = ','):
    with open(filename, 'w', encoding="utf-8") as file:
        for key, value in dict.items():
            file.write('%s:%s\n' % (key, values_splitter.join(value)))

# Задача № 1
def fibonacci(number: int):
    return 1 if number in [1, 2] else fibonacci(number - 1) + fibonacci(number - 2)

# Задача № 2
def input_fruit_first_char(start_with: str = ''):
    return input(f"{start_with}Введите букву (! - для окончания): ").lower()

def get_fruits_dict():
    fruits_lines = get_file_lines("fruits.txt")
    return convert_lines_to_dict(fruits_lines)

# Задача № 3
def get_bot_dict():
    answers_lines = get_file_lines("answers.txt")
    return convert_lines_to_dict(answers_lines, '|')

def input_bot_command(start_with: str = ''):
    return input(f"{start_with}Введите команду: ").lower()

print("Задача № 1")
number = int(input("Введите число: "))
fibonacci_list = [fibonacci(i) for i in range(1, number + 1)]
print(fibonacci_list)

print("\nЗадача № 2")
fruits_dict = get_fruits_dict()
fruit_first_char = input_fruit_first_char()
while (fruit_first_char != "!"):
    fruit_exists = fruit_first_char in fruits_dict
    print(fruits_dict[fruit_first_char] if fruit_exists else "Фрукт, название которого начинается с данной буквы, не найден!")
    fruit_first_char = input_fruit_first_char('\n')

print("\nЗадача № 3")
answers_dict = get_bot_dict()
print("Вы подключились к боту 'Железяка v1.0'\nДля вывода возможных вариантов вопросов введите qlist, для отключения введите exit")
bot_command = input_bot_command()
while (bot_command != "exit"):
    if bot_command == "qlist":
        print(list(answers_dict.keys()))
    elif bot_command in answers_dict:
        answers_list = answers_dict[bot_command]
        print(answers_list[randint(0, len(answers_list) - 1)])
    else:
        studying = input("К сожалению, ответа на данную команду я не имею( Хотите меня обучить (да/нет)?: ").lower()
        if studying == "да":
            answers_list = input("Введите возможные варианты ответов, разделяя символом |: ").split('|')
            answers_dict[bot_command] = answers_list
            write_dict_to_file("answers.txt", answers_dict, '|')
    bot_command = input_bot_command('\n')