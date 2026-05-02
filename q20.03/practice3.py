FILE = "music_collection.txt"

def add_album():
    name = input("Назва альбому: ")
    artist = input("Виконавець: ")
    year = input("Рік: ")

    with open(FILE, "a") as f:
        f.write(f"{name},{artist},{year}\n")

def show_all():
    try:
        with open(FILE, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("Файл порожній або не існує")

def find_by_artist():
    artist = input("Введіть виконавця: ")
    try:
        with open(FILE, "r") as f:
            for line in f:
                name, art, year = line.strip().split(",")
                if art.lower() == artist.lower():
                    print(name, art, year)
    except FileNotFoundError:
        print("Файл не знайдено")

def delete_album():
    name = input("Введіть назву альбому: ")
    try:
        with open(FILE, "r") as f:
            lines = f.readlines()

        with open(FILE, "w") as f:
            for line in lines:
                if not line.startswith(name + ","):
                    f.write(line)
    except FileNotFoundError:
        print("Файл не знайдено")

while True:
    print("\n1 - Додати")
    print("2 - Показати всі")
    print("3 - Пошук")
    print("4 - Видалити")
    print("5 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        add_album()
    elif choice == "2":
        show_all()
    elif choice == "3":
        find_by_artist()
    elif choice == "4":
        delete_album()
    elif choice == "5":
        break
    else:
        print("Невірний вибір")