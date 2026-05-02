import random

set1 = {random.randint(1, 20) for _ in range(10)}
set2 = {random.randint(1, 20) for _ in range(10)}

print(f"Множина 1: {set1}")
print(f"Множина 2: {set2}")

print(f"Спільні елементи: {set1 & set2}")

print(f"Різниця (set1 - set2): {set1 - set2}")

print(f"Об'єднання: {set1 | set2}")