def is_lucky(n):
    if len(str(n)) != 6:
        return False

    first = int(str(n)[0]) + int(str(n)[1]) + int(str(n)[2])
    second = int(str(n)[3]) + int(str(n)[4]) + int(str(n)[5])

    return first == second

print(is_lucky(123420))
print(is_lucky(723422))