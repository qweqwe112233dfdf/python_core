start = int(input("Початок діапазону: "))
end = int(input("Кінець діапазону: "))

print("Усі числа:")
i = start
while i <= end:
    print(i, end=" ")
    i += 1
print("\n")

print("У спадному порядку:")
i = end
while i >= start:
    print(i, end=" ")
    i -= 1
print("\n")

print("Кратні 7:")
i = start
while i <= end:
    if i % 7 == 0:
        print(i, end=" ")
    i += 1
print("\n")

count_5 = 0
i = start
while i <= end:
    if i % 5 == 0:
        count_5 += 1
    i += 1
print(f"чисел, кратних 5: {count_5}")