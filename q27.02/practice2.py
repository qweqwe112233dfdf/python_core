def odd_numbers(a, b):
    for i in range(min(a, b), max(a, b) + 1):
        if i % 2 != 0:
            print(i)

odd_numbers(1, 10)