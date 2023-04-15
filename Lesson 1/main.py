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

day_number = int(input("Введите день недели: "))
print_weekday_name(day_number)