def print_even_numbers(start, end):
    if start > end:
        start, end = end, start
        
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=" ")
    print()

print_even_numbers(2, 11)