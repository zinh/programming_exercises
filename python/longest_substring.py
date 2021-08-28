from typing import Dict

def longest_substringv1(s: str) -> int:
    pos : int = 0
    max_len : int = 0
    current_substring : list[str] = []
    while True:
        if pos >= len(s):
            return max_len
        c = s[pos]
        try:
            idx = current_substring.index(c)
            current_substring = current_substring[(idx+1):]
        except ValueError:
            pass
        finally:
            current_substring.append(c)
            if max_len < len(current_substring):
                max_len = len(current_substring)
        pos += 1
    return len(current_substring)

def longest_substringv2(s: str) -> int:
    chars = [0] * 128
    left = right = 0
    res = 0
    while right < len(s):
        r = s[right]
        chars[ord(r)] += 1
        while chars[ord(r)] > 1:
            l = s[left]
            chars[ord(l)] -= 1
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res

class Solution:
    def longest_substring(s: str) -> int:
        m = [-1] * 128
        left = right = 0
        res = 0
        while right < len(s):
            c_right = ord(s[right])
            if m[c_right] >= left:
                left = m[c_right] + 1
            res = max(res, right - left + 1)
            m[c_right] = right
            right += 1
        return res
