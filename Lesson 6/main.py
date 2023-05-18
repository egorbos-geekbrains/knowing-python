from random import randint

# Задача № 1
def magic_calc(number: int, step: int = 3):
    if step == 1: return number * 3
    else:
        multiplier = 10
        while (number / multiplier) >= 1:
            multiplier *= 10
        temp = 0
        for i in range(1, step):
            temp += number * pow(multiplier, i)
        return temp + magic_calc(number, step - 1)

# Задача № 2
def contains_num_by_digits_in_list(list: list[int], number: str):
    index = 0
    digits = [int(i) for i in number]
    for num in list:
        if num == digits[index]: index += 1
        elif num != digits[0]: index = 0
        if index == 3: return True
    return False

print('Задача № 1')
number = input('Введите число: ')
print(f'{number} + {number*2} + {number*3} = {magic_calc(int(number))}')

print('\nЗадача № 2')
num_list = [randint(0, 9) for _ in range(0, 15)]
print(f'Список: {num_list}')
number = input('Введите число: ')
while (len(number) < 3 or len(number) > 3):
    number = int(input('Число должно быть трёхзначным! Введите число: '))
contains_digits = contains_num_by_digits_in_list(num_list, number)
print(f'Список {"" if contains_digits else "не "}содержит последовательность, совпадающую с введённым числом.')