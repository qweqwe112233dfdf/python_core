start = int(input("Початок: "))
end = int(input("Кінець: "))
step = int(input("Крок: "))
order = input("Порядок (прямий/зворотній): ")

if order == "прямий":
    i = start
    while i <= end:
        print(i, end=" ")
        i += step
else:
    i = end
    while i >= start:
        print(i, end=" ")
        i -= step