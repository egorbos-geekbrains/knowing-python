import numpy as np
from random import randint

print('Задача № 1')
elements = [randint(0, 20) for _ in range(10)]
print(f'Список: {elements}')
print(f'Количество уникальных элементов: {len(np.unique(elements))}')