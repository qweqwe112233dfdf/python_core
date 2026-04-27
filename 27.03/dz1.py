import random
import string

name = input("Введіть своє ім'я: ")

nick1 = name + str(random.randint(100, 9999))

symbols = "_.,"
nick2 = name + random.choice(symbols) + "".join(random.choices(string.ascii_lowercase, k=3))

prefixes = ["Pro", "Super", "Ultra", "Mega", "Dark"]
prefix = random.choice(prefixes)
nick3 = prefix + name[::-1] + str(random.randint(10, 99))

print("\nВаші нікнейми:")
print("1:", nick1)
print("2:", nick2)
print("3:", nick3)