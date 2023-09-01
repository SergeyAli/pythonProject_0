# Функция all()
# all(iterable)
# Функция возвращает истину, если все элементы последовательности являются истиной.
# На Python создание функции all выглядело бы так:
""""all(iterable)"""


def all_(iterable):
    for element in iterable:
        if not element:
            return False
    return True


# Функция all обычно применяется с результатами каких-то вычислений, которые должны быть истинными или ложными.

numbers = [42, -73, 1024]
if all(map(lambda x: x > 0, numbers)):
    print('Все элементы положительные')
else:
    print('В последовательности есть отрицательные и/или нулевые элементы')