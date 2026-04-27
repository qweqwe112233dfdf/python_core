try:
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    print("Результат:", a / b)
except ValueError:
    print("Помилка: введено не число!")
except ZeroDivisionError:
    print("Помилка: ділення на нуль неможливе!")
finally:
    print("Операцію завершено")