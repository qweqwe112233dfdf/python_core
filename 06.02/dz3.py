text = input("Введіть текст: ")
reserved_words = ["програмування", "справи", "код"]

words = text.split()
result_words = []

for word in words:
    clean_word = word.strip(".,!?").lower()
    if clean_word in reserved_words:
        result_words.append(word.upper())
    else:
        result_words.append(word)

print("Результат:", " ".join(result_words))