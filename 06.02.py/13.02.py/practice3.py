numbers = input('Введіть числа через пробіл: ')
numbers = numbers.split()

summa = 0
for i in numbers:
    if int(i) > 0:
        summa += int(i)

print(summa)