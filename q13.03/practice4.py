balance = 10000
try:
    amount = int(input("Введіть суму для зняття: "))
    if amount % 10 != 0 or amount > balance:
        raise Exception("Некоректна сума для зняття")
    print("Гроші видано:", amount)

except ValueError:
    print("Помилка: введіть число")

except Exception as e:
    print("Помилка:", e)

finally:
    print("Транзакцію завершено")