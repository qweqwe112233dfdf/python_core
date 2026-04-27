lst = [10, 20, 30, 40, 50]

try:
    i = int(input("Введіть індекс елемента: "))
    print("Елемент:", lst[i])
except ValueError:
    print("Помилка: індекс не число")
except IndexError:
    print("Помилка: індекс поза межами списку")
finally:
    print("Операцію завершено")