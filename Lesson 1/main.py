from math import sqrt

# Задача № 1
def print_weekday_name(day_number):
    if (day_number < 1 or day_number > 7):
        print("Нет такого дня")
    elif day_number == 1: print("Понедельник")
    elif day_number == 2: print("Вторник")
    elif day_number == 3: print("Среда")
    elif day_number == 4: print("Четверг")
    elif day_number == 5: print("Пятница")
    elif day_number == 6: print("Суббота")
    else: print("Воскресенье")

# Задача № 2
def calc_2d_distance(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

# Задача № 3
def print_quarter_values(quarter):
    if quarter == 1: print("x > 0, y > 0")
    elif quarter == 2: print("x < 0, y > 0")
    elif quarter == 3: print("x < 0, y < 0")
    elif quarter == 4: print("x > 0, y < 0")

# Задача № 4
def print_even_numbers(number):
    numbers = []
    current_number = 2
    while (current_number <= number):
        if current_number % 2 == 0: numbers.append(current_number)
        current_number += 2
    print(numbers)

print("Задача № 1")
day_number = int(input("Введите день недели: "))
print_weekday_name(day_number)

print("\nЗадача № 2")
print("Введите координаты точки A.")
x1 = float(input("Координата X: "))
y1 = float(input("Координата Y: "))
print("Введите координаты точки B.")
x2 = float(input("Координата X: "))
y2 = float(input("Координата Y: "))
distance = calc_2d_distance(x1, y1, x2, y2)
print(f"Результат: {distance:.2f}")

print("\nЗадача № 3")
quarter = int(input("Введите номер четверти: "))
while (quarter < 1 or quarter > 4):
    quarter = int(input("Вы ошиблись!\nВведите номер четверти: "))
print_quarter_values(quarter)

print("\nЗадача № 4")
number = int(input("Введите число: "))
while number < 0:
    number = int(input("Число должно быть положительным!\nВведите число: "))
print_even_numbers(number)