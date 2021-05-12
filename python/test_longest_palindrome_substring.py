import unittest

class TestLongestPalindrome(unittest.TestCase):
    def test_longestPalindrome(self):
        solution = Solution()
        self.assertEqual('bab', solution.longestPalindrome('babad'))
        self.assertEqual('bb', solution.longestPalindrome('cbbd'))
        self.assertEqual('a', solution.longestPalindrome('a'))
        self.assertEqual('a', solution.longestPalindrome('ac'))
