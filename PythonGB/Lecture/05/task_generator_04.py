# List comprehensions
# Что будет, если генераторное выражение записать не в круглых скобках, а в квадратных?
# Получим list comprehensions. Другие названия: list comp, генератор списков, списковое включение.
# И нет, это не генераторное выражение. Генератор списков полностью формирует список с элементами
# до его присваивания переменной слева от знака равно.

my_listcomp = [chr(i) for i in range(97, 123)]
print(my_listcomp) # ['a', 'b', 'c', 'd', ..., z]
for char in my_listcomp:
    print(char)