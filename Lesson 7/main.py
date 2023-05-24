from random import randint
from typing import TypeVar
from collections.abc import Callable, Iterable

# Задача № 1
T = TypeVar('T')
R = TypeVar('R')
def map_to(func: Callable[[T], R], iterable: Iterable[T]):
    return list([func(e) for e in iterable])

# Задача № 2
def repeat_func(count: int):
    def test(func):
        def decorator():
            for _ in range(0, count):
                func()
        return decorator
    return test

print('Задача № 1')
numbers_list = [1, 2, 3, 4, 5]
print(f'Список: {numbers_list}')
numbers_list = map_to(lambda e: e * 10, numbers_list)
print(f'Результат (e: e * 10): {numbers_list}')

print('\nЗадача № 2')
@repeat_func(10)
def test_func(): print('Magic!', end=' ')
test_func()