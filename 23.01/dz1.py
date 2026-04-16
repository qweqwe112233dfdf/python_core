start = int(input("Початок діапазону: "))
end = int(input("Кінець діапазону: "))

while start <= end:
    if start % 7 == 0:
        print(start)
    start += 1