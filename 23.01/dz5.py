a = int(input("Перше число: "))
b = int(input("Друге число: "))

if a > b:
    start, end = b, a
else:
    start, end = a, b

product = 1
found = False

while start <= end:
    if start % 4 == 0 and start % 6 != 0:
        product *= start
        found = True
    start += 1

if found:
    print("Добуток:", product)
else:
    print("Таких чисел у діапазоні немає.")