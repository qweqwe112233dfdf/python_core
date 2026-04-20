import random

list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(10)]

print(f"Список 1: {list1}")
print(f"Список 2: {list2}")

res1 = list1 + list2
print(f"1. усі елементи: {res1}")

res2 = list(set(list1) | set(list2))
print(f"2. Без повторень: {res2}")

res3 = list(set(list1) & set(list2))
print(f"3. спільні для обох списків: {res3}")

res4 = list(set(list1) ^ set(list2))
print(f"4. унікальні: {res4}")

res5 = [min(list1), max(list1), min(list2), max(list2)]
print(f"5. Мінімальне та максимальне значення з кожного списку: {res5}")