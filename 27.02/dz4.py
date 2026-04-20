def count_digits(number):
    return len(str(abs(number)))

result = count_digits(3456)
print(f"Кількість цифр: {result}")