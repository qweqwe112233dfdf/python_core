mark1 = int(input("оцінка 1: "))
mark2 = int(input("оцінка 2: "))
mark3 = int(input("оцінка 3: "))

if mark1 == 2 or mark2 == 2 or mark3 == 2:
    print('незадовільно')
elif mark1 >= 4 and mark2 >= 4 and mark3 >= 4:
    print('відмінно')