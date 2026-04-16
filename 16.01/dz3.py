starter = input("Закуска (салат/суп/нічого): ")
main = input("Основна страва (курка/риба/нічого): ")
dessert = input("Десерт (морозиво/фрукти/нічого): ")
status = input("Ви постійний клієнт?: ")

total = 0
count = 0

if starter == "салат":
    total += 5
    count += 1
elif starter == "суп":
    total += 7
    count += 1

if main == "курка":
    total += 10
    count += 1
elif main == "риба":
    total += 12
    count += 1

if dessert == "морозиво":
    total += 3
    count += 1
elif dessert == "фрукти":
    total += 4
    count += 1

if starter == "суп" and main == "риба" and (dessert == "морозиво" or dessert == "фрукти"):
    total -= 2

if main == "курка" and dessert == "морозиво":
    print("Подарунок: Чай")

discount = 0

if count == 3:
    discount = 10

if total > 20:
    discount = 15

if status == "так":
    discount += 5

final_total = total - (total * discount / 100)

print("До сплати:", final_total, "$")