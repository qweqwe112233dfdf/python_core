contacts = {}

while True:
    print("\n1. Додати 2. Видалити 3. Змінити 4. Показати всі 5. Вихід")
    choice = input("Оберіть дію: ")

    if choice == "1":
        name = input("Ім'я: ")
        phone = input("Телефон: ")
        contacts[name] = phone
    elif choice == "2":
        name = input("Яке ім'я видалити?: ")
        contacts.pop(name, "Контакт не знайдено")
    elif choice == "3":
        name = input("Яке ім'я змінити?: ")
        if name in contacts:
            contacts[name] = input("Новий номер: ")
        else:
            print("Немає такого контакту")
    elif choice == "4":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == "5":
        break