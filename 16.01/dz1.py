number = int(input("Введіть число: "))
stepin = int(input("Введіть степінь (від 0 до 7): "))

if 0 <= stepin <= 7:
    result = number ** stepin
    print(result)
else:
    print("помилка!")