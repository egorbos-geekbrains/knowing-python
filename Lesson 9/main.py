import numpy as np
from random import randint

# Вспомогательные функции
def build_list():
    return [randint(1, 2) for _ in range(5)]

print('Задача № 1')
elements = [randint(0, 20) for _ in range(10)]
print(f'Список: {elements}')
print(f'Количество уникальных элементов: {len(np.unique(elements))}')

print('\nЗадача № 2')
matrix = np.array([build_list() for _ in range(1, 6)], dtype=int)
unique_rows = np.unique(matrix, axis=0)
print(f'Матрица:\n{matrix}')
print(f"Одинаковые строки {'присутствуют' if len(matrix) - len(unique_rows) > 0 else 'отстствуют'}")