from random import randint

# Задача № 2
def get_ascending_sequences(num_list: list):
    result = [[num_list[0]]]
 
    for i in range(1, len(num_list)):
        if num_list[i - 1] < num_list[i]:
            result[-1].append(num_list[i])
 
        else:
            result.append([num_list[i]])

    return list(filter(lambda e: len(e) > 1, result))

print("Задача № 1")
numbers = [randint(1, 10) for _ in range(7)]
print(f"Оригинальный список: {numbers}")
greater_five_list = list(filter(lambda e: e > 5, numbers))
print(f"Список со значениями больше пяти: {greater_five_list}")

print("\nЗадача № 2")
numbers = [randint(1, 10) for _ in range(9)]
print(f"Оригинальный список: {numbers}")
print("Возрастающие последовательности: ", end='')
print(*get_ascending_sequences(numbers), sep=', ')

print("\nЗадача № 3")
numbers = [randint(1, 10) for _ in range(9)]
print(f"Оригинальный список: {numbers}")
count_dict = {i: numbers.count(i) for i in numbers}
unique_count = sum(filter(lambda e: e > 1, count_dict.values()))
print(f"{unique_count} элемента(ов) совпадают, список уникальных элементов - {list(count_dict.keys())}")