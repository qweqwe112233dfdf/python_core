import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


def menu():
    while True:
        print("\nМеню:")
        print("1. Коло")
        print("2. Прямокутник")
        print("3. Трикутник")
        print("0. Вихід")

        choice = input("Оберіть фігуру: ")

        if choice == "1":
            r = float(input("Введіть радіус: "))
            c = Circle(r)
            print("Площа:", c.area())
            print("Периметр:", c.perimeter())

        elif choice == "2":
            a = float(input("Введіть сторону a: "))
            b = float(input("Введіть сторону b: "))
            r = Rectangle(a, b)
            print("Площа:", r.area())
            print("Периметр:", r.perimeter())

        elif choice == "3":
            a = float(input("Введіть сторону a: "))
            b = float(input("Введіть сторону b: "))
            c = float(input("Введіть сторону c: "))
            t = Triangle(a, b, c)
            print("Площа:", t.area())
            print("Периметр:", t.perimeter())

        elif choice == "0":
            print("Вихід")
            break
        else:
            print("Невірний вибір!")

menu()