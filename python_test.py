"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('python').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing for max INT"""

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 8, 12, 48]), 48)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([69, 420, 350]), 420)
        self.assertEqual(max_integer([3]), 3)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_none(self):
        self.assertIsNone(max_integer([]))

    def test_type(self):
        self.assertRaises(TypeError, max_integer((1, 2)))


if __name__ == '__main__':
    unittest.main()
