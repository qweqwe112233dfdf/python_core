dictionary = {
    "apple": "яблуко",
    "computer": "комп'ютер",
    "programming": "програмування",
    "game": "гра",
    "friend": "друг"
}

word = input("Введіть англійське слово: ").lower().strip()

if word in dictionary:
    print(f"Переклад: {dictionary[word]}")
else:
    print("Слово не знайдено.")