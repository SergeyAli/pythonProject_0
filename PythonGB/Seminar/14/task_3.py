'''
Задание №3
📌 Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
📌 возврат строки без изменений
📌 возврат строки с преобразованием регистра без потери символов
📌 возврат строки с удалением знаков пунктуации
📌 возврат строки с удалением букв других алфавитов
📌 возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
'''

from task_2 import deleter_simbols
import unittest

class TestUnit(unittest.TestCase):
    def test_method(self):
        self.assertEqual(deleter_simbols('hello world'), 'hello world')
    def test_sym(self):
        self.assertEqual(deleter_simbols('Hello World'), 'hello world')
    def test_znak(self):
        self.assertEqual(deleter_simbols('Hello, World!'), 'hello world')
    def test_lang(self):
        self.assertEqual(deleter_simbols('Hello wяrld'), 'hello wrld')
    def test_all(self):
        self.assertEqual(deleter_simbols('Hello%, Wяr&ld!'), 'hello wrld')

if __name__ == '__main__':
    unittest.main(verbosity=2)
