# Задача № 1
def get_factorial(number: int):
    return 1 if number == 1 else number * get_factorial(number - 1)

print("Задача № 1")
number = int(input("Введите число: "))
factorials = [get_factorial(i) for i in range(1, number + 1)]
print(factorials)