dictionary = {
    "hello": "привіт",
    "cat": "кіт",
    "dog": "собака"
}

word = input("Слово англійською: ")

print(dictionary.get(word, "Слово не знайдено"))