try:
    order = input("Введіть номер замовлення: ")
    if not (order.startswith("ORD") and order[3:].isdigit()):
        raise Exception("Неправильний формат номера замовлення")

    print("Номер прийнято:", order)

except Exception as e:
    print("Помилка:", e)

finally:
    print("Перевірку завершено")