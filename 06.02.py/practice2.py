text = input('введіть текст: ')
symbol = input('введіть символ: ')

count = 0
for c in text:
    if c == symbol:
        count += 1

print(count)