import unittest
from longest_substring import longest_substring

class LongestSubstringTest(unittest.TestCase):
    def test_longest_substring(self):
        self.assertEqual(3, longest_substring('abcabcbb'))
        self.assertEqual(1, longest_substring('bbb'))
        self.assertEqual(3, longest_substring('pwwkew'))
        self.assertEqual(2, longest_substring('aab'))
