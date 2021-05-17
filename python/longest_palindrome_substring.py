class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(0, len(s)):
            for j in range(i + 1, len(s)):
                if (i + j) % 2 == 0:
                    pass
                else:
                    middle = (i + j) // 2


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome('aaaa'))
