price = int(input("введіть суму покупки: "))
age = int(input("введіть свій вік: "))

if age < 18:
    discount = 0.10
elif 18 <= age <= 60:
    discount = 0.05
else:
    discount = 0.15

total = price * (1 - discount)
print(f"сума до сплати зі знижкою: {total}")