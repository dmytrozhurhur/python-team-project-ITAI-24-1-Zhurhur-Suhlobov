import unittest
import sys
import os

from generator import generate_password, assess_strength

class TestPasswordGenerator(unittest.TestCase):
    def test_length(self):
        pwd = generate_password(10, True, True, True)
        self.assertEqual(len(pwd), 10)

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(0, True, True, True)

    def test_strength_weak(self):
        self.assertEqual(assess_strength("abc"), "Слабкий")

if __name__ == '__main__':
    unittest.main()