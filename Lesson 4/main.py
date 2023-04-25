from math import sqrt

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

print("Задача № 1")
number = int(input("Введите число: "))
prime_factors_list = get_prime_factors(number)
print(prime_factors_list, f"-> {len(prime_factors_list)} шт.")

print("\nЗадача № 2")
icecream = read_file_lines("icecream.txt")
assortment = set(split_list_values(icecream[0]))
in_stock = set(split_list_values(icecream[1]))
print(f"Закончилось: {', '.join(assortment.difference(in_stock))}")