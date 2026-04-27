import os

FILE_NAME = 'orders.txt'

def read_orders():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as f:
        return [line.strip().split(',') for line in f.readlines()]

def save_orders(orders):
    with open(FILE_NAME, 'w') as f:
        for order in orders:
            f.write(','.join(order) + '\n')

while True:
    print("\nМеню")
    print("1. Додати нове замовлення")
    print("2. Переглянути всі замовлення")
    print("3. Пошук за номером")
    print("4. Оновити замовлення")
    print("5. Видалити замовлення")
    print("6. Вихід")
    
    choice = input("Оберіть дію: ")

    if choice == '1':
        number = input("Номер замовлення: ")
        name = input("Назва товару: ")
        amount = input("Кількість: ")
        price = input("Ціна: ")
        with open(FILE_NAME, 'a') as f:
            f.write(f"{number},{name},{amount},{price}\n")
        print("Замовлення додано!")

    elif choice == '2':
        orders = read_orders()
        for o in orders:
            print(f"№{o[0]} | Товар: {o[1]} | Кількість: {o[2]} | Ціна: {o[3]}")

    elif choice == '3':
        num = input("Введіть номер для пошуку: ")
        orders = read_orders()
        found = [o for o in orders if o[0] == num]
        if found:
            print(f"Знайдено: {found[0]}")
        else:
            print("Замовлення не знайдено.")

    elif choice == '4':
        num = input("Введіть номер замовлення для оновлення: ")
        orders = read_orders()
        for o in orders:
            if o[0] == num:
                o[2] = input("Нова кількість: ")
                o[3] = input("Нова ціна: ")
        save_orders(orders)
        print("Дані оновлено.")

    elif choice == '5':
        num = input("Введіть номер замовлення для видалення: ")
        orders = read_orders()
        orders = [o for o in orders if o[0] != num]
        save_orders(orders)
        print("Замовлення видалено (якщо воно існувало).")

    elif choice == '6':
        break
    else:
        print("Неправильний вибір.")