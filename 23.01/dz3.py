start = int(input("Початок діапазону: "))
end = int(input("Кінець діапазону: "))

while start <= end:
    if start % 3 == 0 and start % 5 == 0:
        print("Fizz Buzz")
    elif start % 3 == 0:
        print("Fizz")
    elif start % 5 == 0:
        print("Buzz")
    else:
        print(start)
    start += 1