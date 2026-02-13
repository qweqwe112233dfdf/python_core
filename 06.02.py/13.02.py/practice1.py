numbers = input('Введіть числа через пробіл: ')
numbers = numbers.split()

summa = 0
for i in numbers:
    summa += int(i)

average = summa / len(numbers)

print(summa)
print(average)