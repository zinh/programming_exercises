def halve(lst):
    if len(lst) % 2 != 0:
        raise BaseException("list should have even length")
    return [lst[0:len(lst)//2], lst[len(lst)//2:]]

def is_palindrome(x: int) -> bool:
    n : int = 0;
    while x > 0:
        digit = x % 10;
        n = n * 10 + digit;
        x = x // 10;
    print(n)
    return n == x;
