'''
Чтение файла: целиком, через генератор
Рассмотрим подробнее варианты чтения информации из файла.
● Чтение в список
'''

with open('text_data.txt', 'r', encoding='utf-8') as f:
    print(list(f))
