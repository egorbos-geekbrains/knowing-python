# Задача № 1
def get_factorial(number: int):
    return 1 if number == 1 else number * get_factorial(number - 1)

# Задача № 4
def shift(list, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            list.append(list.pop(0))
    else:
        for i in range(steps):
            list.insert(0, list.pop())

print("Задача № 1")
number = int(input("Введите число: "))
factorials = [get_factorial(i) for i in range(1, number + 1)]
print(factorials)

print("\nЗадача № 2")
print("| X | Y | Z | ¬(X ∧ Y) ∨ Z |")
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"| {x} | {y} | {z} |       {int(not (x and y) or z)}      |")

print("\nЗадача № 3")
count_dict = {}
first_line = input("Введите первую строку: ").lower()
second_line = input("Введите вторую строку: ").lower()
for char in first_line:
    count_dict[char] = second_line.count(char)
print(count_dict)

print("\nЗадача № 4")
number = abs(int(input("Введите число: ")))
numbers = [i for i in range(-number, number + 1)]
shift(numbers, 2)
print(numbers)