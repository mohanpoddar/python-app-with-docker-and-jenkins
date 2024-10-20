import unittest
from app.calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 5

    def test_add(self):
        self.assertEqual(add(self.a, self.b), 15)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(self.a, self.b), 5)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(self.a, self.b), 2)
        self.assertEqual(divide(-10, 2), -5)
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
