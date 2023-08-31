'''
Задание №2
📌 Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
'''

import re
import doctest


def deleter_simbols(text: str):
    '''
    deleter all ...
    >>> deleter_simbols('hello')
    'hello'
    >>> deleter_simbols('Hello')
    'hello'
    >>> deleter_simbols('hello, kitty!')
    'hello kitty'
    >>> deleter_simbols('hello кат')
    'hello '
    >>> deleter_simbols('Hello, кат!')
    'hello '


    '''
    regex = re.compile('[^a-zA-Z ]')
    return regex.sub('', text).lower()


if __name__ == '__main__':
    print(deleter_simbols('ge!!w me 23qw water'))
    doctest.testmod(verbose=True)
