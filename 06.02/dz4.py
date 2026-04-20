text = input("Введіть рядок: ")
char1 = input("Введіть перший символ: ")
char2 = input("Введіть другий символ: ")

start_index = text.find(char1)
end_index = text.find(char2)

if start_index != -1 and end_index != -1:
    new_string = text[:start_index] + text[end_index + 1:]
    print("Результат:", new_string)
else:
    print("Один з символів не знайдено.")