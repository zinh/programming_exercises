import unittest
from longest_substring import longest_substringv1

class LongestSubstringTest(unittest.TestCase):
    def test_longest_substring(self):
        self.assertEqual(3, longest_substringv1('abcabcbb'))
        self.assertEqual(1, longest_substringv1('bbb'))
        self.assertEqual(3, longest_substringv1('pwwkew'))
        self.assertEqual(2, longest_substringv1('aab'))
