# ------------------------------------------- 6 -----------------------------
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировки Unicode
# Текст выравнивается по правому краю так,
# чтобы у самого длинного слова был один пробел между ним и номером строки

texts = sorted(input('Введите несколько слов: ').split())

max_len = 0
for world in texts:
    if len(world) > max_len:
        max_len = len(world)

for i, world in enumerate(texts, 1):
    print(f'{i}. {world:>{max_len}}')
