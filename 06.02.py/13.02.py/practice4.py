numbers = input('Введіть числа через пробіл: ')
numbers = numbers.split()

for i in range(len(numbers)):
    if int(numbers[i]) % 2 == 0:
        print(i, end=", ")