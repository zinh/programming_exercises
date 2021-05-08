def halve(lst):
    if len(lst) % 2 != 0:
        raise BaseException("list should have even length")
    return [lst[0:len(lst)//2], lst[len(lst)//2:]]
