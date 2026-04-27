import console_ui

def main():
    console_ui.draw_header("СУПЕР ГРА 2026")

    options = [
        "Нова гра",
        "Завантажити збереження",
        "Вихід"
    ]

    console_ui.draw_menu(options)

    choice = input("\nВаш вибір: ")

    if choice not in ["1", "2", "3"]:
        console_ui.draw_warning("Невірний вибір!")

if __name__ == "__main__":
    main()