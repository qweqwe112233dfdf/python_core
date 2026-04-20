text = input("Введіть текст: ")
symbols = input("Введіть набір символів (без пробілів): ")

words = text.split()
filtered_words = []

for word in words:
    contains_symbol = any(char in word for char in symbols)
    if not contains_symbol:
        filtered_words.append(word)

print("Результат:", " ".join(filtered_words))