text = input('введіть текст: ')
slovo = input('введіть слово для пошуку: ')

if slovo in text:
    counter = 0
    while counter < slovo:
        counter += 1
print(counter)