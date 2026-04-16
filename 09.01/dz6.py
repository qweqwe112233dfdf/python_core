age = int(input("Введіть вік автомобіля: "))
mileage = int(input("Введіть пробіг автомобіля: "))

if age < 3 and mileage <= 30000:
    print("Автомобіль у відмінному стані")
elif age <= 10 and mileage <= 100000:
    print("Автомобіль у хорошому стані")
else:
    print("Автомобіль потребує перевірки")