# Задача № 1
def fibonacci(number: int):
    return 1 if number in [1, 2] else fibonacci(number - 1) + fibonacci(number - 2)

print("Задача № 1")
number = int(input("Введите число: "))
fibonacci_list = [fibonacci(i) for i in range(1, number + 1)]
print(fibonacci_list)