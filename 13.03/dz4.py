import math

try:
    x = float(input("Введіть число: "))
    if x < 0:
        raise Exception("Не можна обчислити квадратний корінь від'ємного числа")
    print("Корінь:", math.sqrt(x))
except ValueError:
    print("Помилка: не число")
except Exception as Exception:
    print("Помилка:", Exception)
finally:
    print("Обчислення завершено")