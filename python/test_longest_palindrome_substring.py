import unittest
from longest_palindrome_substring import Solution

class TestLongestPalindrome(unittest.TestCase):
    @unittest.skip("skip")
    def test_longestPalindrome(self):
        solution = Solution()
        self.assertEqual('bab', solution.longestPalindrome('babad'))
        self.assertEqual('bb', solution.longestPalindrome('cbbd'))
        self.assertEqual('a', solution.longestPalindrome('a'))
        self.assertEqual('a', solution.longestPalindrome('ac'))
        self.assertEqual('bb', solution.longestPalindrome('bb'))
        self.assertEqual('ccc', solution.longestPalindrome('ccc'))
        self.assertEqual('bb', solution.longestPalindrome('abb'))
        self.assertEqual('aaaa', solution.longestPalindrome('aaaa'))
