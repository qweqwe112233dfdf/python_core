try:
    data = input("Введіть товар (назва, ціна, кількість): ")
    name, price, amount = data.split(",")
    price = float(price)
    qty = int(amount)
    print("Товар:", name, price, qty)
except ValueError:
    print("Помилка: неправильний формат")
finally:
    print("Парсинг завершено")