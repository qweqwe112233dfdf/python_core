word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

if set(word1) == set(word2):
    print("Це анаграми")
else:
    print("Це не анаграми")