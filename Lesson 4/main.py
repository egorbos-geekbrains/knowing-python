import re
from math import sqrt, pi

# Вспомогательные функции
def read_file_lines(filename: str):
    with open(filename, encoding="utf-8") as file:
        return file.readlines()

def split_list_values(text: str, values_splitter: str = ','):
    return text.strip().rstrip('\n').split(values_splitter)

# Задача № 1
def get_prime_factors(number: int):
    result = []

    while number % 2 == 0:
        result.append(2)
        number = number / 2
        
    for i in range(3, int(sqrt(number)) + 1, 2):
        while number % i == 0:
            result.append(i)
            number = number / i

    if number > 2:
        result.append(int(number))
    
    return result

# Задача № 4
def convert_group_value(value: str):
    if value == None: return 0
    elif value.replace(' ', '') == '+': return 1
    elif value.replace(' ', '') == '-': return -1
    else: return int(value.replace(' ', ''))

def get_polynomial_values(text: str):
    regexp = r"(?:(?P<first>\-?\d*)x\^2)*(?:(?P<second>\s*[\-?\+?]\s*\d*)x)*(?P<third>\s*[\-?\+?]\s*\d*)*"
    result = re.match(regexp, text)
    first_value = convert_group_value(result.group('first'))
    second_value = convert_group_value(result.group('second'))
    third_value = convert_group_value(result.group('third'))
    return (first_value, second_value, third_value)

def summ_polynomials(*polynomials: tuple):
    first_value = polynomials[0][0] + polynomials[1][0]
    second_value = polynomials[0][1] + polynomials[1][1]
    third_value = polynomials[0][2] + polynomials[1][2]
    return (first_value, second_value, third_value)

def convert_polynomial_to_string(polynomial: tuple):
    result = ''
    part_number = 0
    for part in polynomial:
        if part_number == 0:
            result += f'{part}x^2'
        elif part_number == 1 and part != 0:
            part_value = int(sqrt(pow(part, 2)))
            result += f' {"+" if part > 0 else "-"} {part_value if part_value != 1 else ""}x'
        elif part_number == 2 and part != 0:
            part_value = int(sqrt(pow(part, 2)))
            result += f' {"+" if part > 0 else "-"} {part_value}'
        part_number += 1
    return result

print("Задача № 1")
number = int(input("Введите число: "))
prime_factors_list = get_prime_factors(number)
print(prime_factors_list, f"-> {len(prime_factors_list)} шт.")

print("\nЗадача № 2")
icecream = read_file_lines("icecream.txt")
assortment = set(split_list_values(icecream[0]))
in_stock = set(split_list_values(icecream[1]))
print(f"Закончилось: {', '.join(assortment.difference(in_stock))}")

print("\nЗадача № 3")
precision = int(input("Введите точность вывода: "))
print(f"Результат: {round(pi, precision)}")

print("\nЗадача № 4")
polynomials = read_file_lines("polynomials.txt")
first_polynomial = get_polynomial_values(polynomials[0])
second_polynomial = get_polynomial_values(polynomials[1])
summ = summ_polynomials(first_polynomial, second_polynomial)
print(convert_polynomial_to_string(summ))