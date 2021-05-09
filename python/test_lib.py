import unittest
from lib import halve, is_palindrome

class HalveTest(unittest.TestCase):
    def test_halve(self):
        self.assertEqual(2, 1 + 1)
        self.assertEqual([[1,2],[3,4]], halve([1,2,3,4]))
        self.assertEqual([[1,2],[3,4]], halve([1,2,3,4]))

        with self.assertRaises(BaseException, msg = "list should have even length"):
            halve([1,2,3])

    def test_palidrome(self):
        self.assertEqual(True, is_palindrome(101))
        self.assertEqual(False, is_palindrome(1010))
        self.assertEqual(False, is_palindrome(-121))
