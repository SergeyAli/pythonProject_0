'''
Подготовка теста и сворачивание работ
Иногда бывает необходимо выполнить какие-то действия до начала тестирования, развернуть тестируемую среду. А после
завершения теста наоборот, убрать лишнее. Для этих целей в unittest есть зарезервированные имена методов setUp
и tearDown. Часто их называют фикстурами.
➢ Метод setUp
Когда внутри класса есть несколько тестовых методов, вызов метода setUp происходит перед каждым вызовом теста.
'''

import unittest
class TestSample(unittest.TestCase):

    def setUp(self) -> None:
        self.data = [2, 3, 5, 7]
        print('Выполнил setUp') # Только для демонстрации работы метода

    def test_append(self):
        self.data.append(11)
        self.assertEqual(self.data, [2, 3, 5, 7, 11])

    def test_remove(self):
        self.data.remove(5)
        self.assertEqual(self.data, [2, 3, 7])

    def test_pop(self):
        self.data.pop()
        self.assertEqual(self.data, [2, 3, 5])

if __name__ == '__main__':
    unittest.main()
