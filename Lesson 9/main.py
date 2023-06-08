import numpy as np
from random import randint

# Вспомогательные функции
def build_list(elements_count: int, max_value: int):
    return [randint(0, max_value) for _ in range(elements_count)]

print('Задача № 1')
elements = [randint(0, 20) for _ in range(10)]
print(f'Список: {elements}')
print(f'Количество уникальных элементов: {len(np.unique(elements))}')

print('\nЗадача № 2')
matrix = np.array([build_list(5, 1) for _ in range(5)], dtype=int)
unique_rows = np.unique(matrix, axis=0)
print(f'Матрица:\n{matrix}')
print(f"Одинаковые строки {'присутствуют' if len(matrix) - len(unique_rows) > 0 else 'отстствуют'}")

print('\nЗадача № 3')
length = randint(2, 5)
matrix = np.array([build_list(length, 9) for _ in range(length)], dtype=int)
print(f'Матрица:\n{matrix}')
print(f'Главная диагональ: {np.diagonal(matrix)}')
print(f'Минимальный элемент: {np.argmin(matrix)}, максимальный элемент: {np.argmax(matrix)}')