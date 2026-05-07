import random

# Завантаження слів з файлу
def load_words(filename):
    try:
        with open(filename, "r") as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print("Файл зі словами не знайдено!")
        return ["python", "error", "compiler"]

# Збереження історії гри
def save_result(filename, word, attempts, result):
    with open(filename, "a") as file:
        file.write(f"Слово: {word}, Спроб: {attempts}, Результат: {result}\n")

# Показ стану слова
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Основна гра
def play_game():
    words = load_words("words.txt")
    secret_word = random.choice(words)
    
    guessed_letters = set()
    attempts = 6

    print("Гра 'Шибениця' почалась!")

    while attempts > 0:
        print("\nСлово:", display_word(secret_word, guessed_letters))
        print("Використані літери:", ", ".join(guessed_letters))
        print("Залишилось спроб:", attempts)

        guess = input("Введіть букву або слово: ").lower()

        # Перевірка введення
        if not guess.isalpha():
            print("Вводьте тільки літери!")
            continue

        # Вгадування слова
        if len(guess) > 1:
            if guess == secret_word:
                print("Вітаю! Ви вгадали слово!")
                save_result("history.txt", secret_word, attempts, "Перемога")
                return
            else:
                print("Неправильно!")
                attempts -= 1
        else:
            if guess in guessed_letters:
                print("Ви вже вводили цю букву!")
                continue

            guessed_letters.add(guess)

            if guess not in secret_word:
                print("Немає такої букви!")
                attempts -= 1

        # Перевірка перемоги
        if all(letter in guessed_letters for letter in secret_word):
            print("\nСлово:", secret_word)
            print("Вітаю! Ви перемогли!")
            save_result("history.txt", secret_word, attempts, "Перемога")
            return

    print("\nВи програли! Слово було:", secret_word)
    save_result("history.txt", secret_word, attempts, "Поразка")


# Перегляд історії
def show_history():
    try:
        with open("history.txt", "r") as file:
            print("\nІсторія ігор:")
            print(file.read())
    except FileNotFoundError:
        print("Історія поки відсутня.")


# Меню
def main():
    while True:
        print("\n1. Грати")
        print("2. Історія")
        print("3. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("До побачення!")
            break
        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main()