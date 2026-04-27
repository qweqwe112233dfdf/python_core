class Book:
    def __init__(self, title, authors, year):
        self.title = title
        self.authors = authors
        self.year = year

    def __str__(self):
        authors_str = ", ".join(self.authors)
        return f"'{self.title}' — {authors_str} ({self.year})"


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книгу '{book.title}' додано до бібліотеки.")

    def remove_book(self, title):
        original_count = len(self.books)
        self.books = [b for b in self.books if b.title.lower() != title.lower()]
        if len(self.books) < original_count:
            print(f"Книгу '{title}' видалено.")
        else:
            print("Книгу не знайдено.")

    def show_all_books(self):
        if not self.books:
            print("Бібліотека порожня.")
        else:
            print(f"\nКниги у '{self.name}':")
            for book in self.books:
                print(book)

    def find_by_title(self, title):
        results = [b for b in self.books if title.lower() in b.title.lower()]
        return results

    def find_by_author(self, author):
        results = []
        for b in self.books:
            if any(author.lower() in a.lower() for a in b.authors):
                results.append(b)
        return results

    def __str__(self):
        return f"Бібліотека: {self.name}, Адреса: {self.address}. Кількість книг: {len(self.books)}"


def main():
    my_lib = Library("Бібліотека", "вул. Шевченко, 1")

    while True:
        print(f"\n{my_lib.name}")
        print("1. Додати книгу")
        print("2. Видалити книгу за назвою")
        print("3. Показати всі книги")
        print("4. Пошук за назвою")
        print("5. Пошук за автором")
        print("6. Інформація про бібліотеку")
        print("0. Вихід")

        choice = input("Оберіть дію: ")

        if choice == '1':
            title = input("Назва книги: ")
            authors = input("Автори (через кому): ").split(',')
            authors = [a.strip() for a in authors]
            year = input("Рік видання: ")
            my_lib.add_book(Book(title, authors, year))

        elif choice == '2':
            title = input("Яку книгу видалити? ")
            my_lib.remove_book(title)

        elif choice == '3':
            my_lib.show_all_books()

        elif choice == '4':
            title = input("Введіть назву для пошуку: ")
            res = my_lib.find_by_title(title)
            for b in res: print(b)

        elif choice == '5':
            author = input("Введіть ім'я автора: ")
            res = my_lib.find_by_author(author)
            for b in res: print(b)

        elif choice == '6':
            print(my_lib)

        elif choice == '0':
            break
        else:
            print("Неправильний вибір.")

if __name__ == "__main__":
    main()