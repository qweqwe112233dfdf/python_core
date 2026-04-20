text = input("Введіть текст: ")
words = text.split()

reversed_words = words[::-1]

result = " ".join(reversed_words)
print("Результат:", result)
