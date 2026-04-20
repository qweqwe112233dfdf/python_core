text = input("Введіть текст для перевірки на паліндром: ")
clean_text = text.replace(" ", "")

if clean_text == clean_text[::-1]:
    print("паліндром!")
else:
    print("не паліндром.")