import sys

sys.path.append("../test-gestform")
from divided_by import *
import unittest


class TestMethods(unittest.TestCase):
    def test_random_integers(self):
        number_list = generate_random_integers()
        self.assertIsInstance(number_list, list)
        self.assertEqual(len(number_list), 10)
        for n in number_list:
            self.assertGreaterEqual(n, -1000)
            self.assertLessEqual(n, 1000)

    def test_is_geste(self):
        self.assertTrue(is_geste(3))
        self.assertTrue(is_geste(-3))
        self.assertTrue(is_geste(15))
        self.assertTrue(is_geste(3333))
        self.assertFalse(is_geste(1))
        self.assertFalse(is_geste(73))
        self.assertFalse(is_geste(3332))

    def test_is_forme(self):
        self.assertTrue(is_forme(5))
        self.assertTrue(is_forme(-5))
        self.assertTrue(is_forme(15))
        self.assertTrue(is_forme(5555))
        self.assertFalse(is_forme(1))
        self.assertFalse(is_forme(73))
        self.assertFalse(is_forme(5554))


if __name__ == "__main__":
    unittest.main()
