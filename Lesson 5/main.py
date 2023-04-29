from random import randint

print("Задача № 1")
numbers = [randint(1, 10) for _ in range(7)]
print(f"Оригинальный список: {numbers}")
greater_five_list = list(filter(lambda e: e > 5, numbers))
print(f"Список со значениями больше пяти: {greater_five_list}")