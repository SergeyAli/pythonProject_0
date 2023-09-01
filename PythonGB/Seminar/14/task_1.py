'''
Задание №1
📌 Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
📌 Возвращается строка в нижнем регистре.
'''

import re
def delsymbol(text: str):
    regex = re.compile('[^a-zA-Z ]')
    return regex.sub('',text).lower()
if __name__ == '__main__':
    print(delsymbol('Give me! a cup of wa&ter!'))
