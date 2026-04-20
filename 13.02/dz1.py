numbers = input("введіть числа через пробіл: ").split()
n = int(input("введіть кількість позицій для зсуву списку: "))

list = [int(x) for x in numbers]

if len(list) > 0:

    n = n % len(list)
    
    shifted_list = list[-n:] + list[:-n]
    
    print(f"Результат: {shifted_list}")