mark1 = int(input("Оцінка 1: "))
mark2 = int(input("Оцінка 2: "))
mark3 = int(input("Оцінка 3: "))
mark4 = int(input("Оцінка 4: "))

if mark1 < 3 or mark2 < 3 or mark3 < 3 or mark4 < 3:
    print("Студент не допускається до іспиту")
elif mark1 >= 4 and mark2 >= 4 and mark3 >= 4 and mark4 >= 4:
    print("Студент допускається до іспиту з відзнакою")
else:
    print("Студент допускається до іспиту")