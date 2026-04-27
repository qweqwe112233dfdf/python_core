def is_symmetric(lst):
    if len(lst) <= 1:
        return True
    if lst[0] != lst[-1]:
        return False
    return is_symmetric(lst[1:-1])

print(is_symmetric([1, 2, 3, 2, 1]))