import unittest

def my_function(x, y):
    z = 0
    if x < 0 or y > 0:
        z += 1
    return z

class TestMyFunction(unittest.TestCase):

    def test_operators(self):
        # Тесты для покрытия операторов
        self.assertEqual(my_function(-1, 1), 1)  # x < 0 и y > 0
        self.assertEqual(my_function(1, 1), 1)    # x > 0 и y > 0
        self.assertEqual(my_function(-1, -1), 1)  # x < 0 и y < 0
        self.assertEqual(my_function(1, -1), 0)   # x > 0 и y < 0
        self.assertEqual(my_function(0, 0), 0)    # x = 0 и y = 0

    def test_branches(self):
        # Тесты для покрытия ветвей (решений)
        self.assertEqual(my_function(-1, 1), 1)   # Оба условия истинны
        self.assertEqual(my_function(1, 1), 1)   # Только одно условие истинно
        self.assertEqual(my_function(1, -1), 0)    # Оба условия ложны

if __name__ == '__main__':
    unittest.main()
