a = int(input("Введіть число A: "))
n = int(input("Введіть ступінь N: "))

result = 1
count = 0

while count < n:
    result *= a
    count += 1

print(result)