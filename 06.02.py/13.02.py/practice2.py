numbers = input('Введіть числа через пробіл: ')
numbers = numbers.split()

poshuk = int(input('Введіть число для пошуку: '))

count = 0
for i in numbers:
    if int(i) == poshuk:
        count = count + 1

print(count)