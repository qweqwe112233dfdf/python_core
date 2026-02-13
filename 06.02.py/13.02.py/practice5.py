numbers = input('Введіть числа через пробіл: ')
numbers = numbers.split()

unique = []

for i in numbers:
    if int(i) not in unique:
        unique.append(int(i))

print(unique)