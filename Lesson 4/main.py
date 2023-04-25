from math import sqrt

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
print(prime_factors_list)