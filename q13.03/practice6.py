try:
    data = input("Введіть числа через пробіл: ")
    numbers = data.split()

    valid_numbers = []

    for x in numbers:
        try:
            num = float(x)
            valid_numbers.append(num)
        except ValueError:
            print("Пропущено некоректне значення:", x)

    if len(valid_numbers) == 0:
        raise ZeroDivisionError("Список порожній")

    total = sum(valid_numbers)
    average = total / len(valid_numbers)

    print("Сума:", total)
    print("Середнє:", average)

except ZeroDivisionError as e:
    print("Помилка:", e)

finally:
    print("Обробку завершено")