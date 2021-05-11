def longest_substring(s: str) -> int:
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
