try:
    data = input("Введіть числа через пробіл: ")
    nums = list(map(int, data.split()))
    print("Сума:", sum(nums))
except ValueError:
    print("Помилка: некоректне введення")
finally:
    print("Обробку завершено")