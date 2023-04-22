# Вспомогательные функции
def get_file_lines(filename: str):
    data = open(filename, encoding="utf-8")
    lines = data.readlines()
    data.close()
    return lines

def split_key_value(text: str):
    splitted = text.split(':')
    return (splitted[0], splitted[1].rstrip('\n').split(','))

def convert_lines_to_dict(lines: list[str]):
    pairs = [split_key_value(line) for line in lines]
    return dict(pairs)

# Задача № 1
def fibonacci(number: int):
    return 1 if number in [1, 2] else fibonacci(number - 1) + fibonacci(number - 2)

# Задача № 2
def input_fruit_first_char(start_with: str = ''):
    return input(f"{start_with}Введите букву (! - для окончания): ").lower()

def get_fruits_dict():
    fruits_lines = get_file_lines("fruits.txt")
    return convert_lines_to_dict(fruits_lines)

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