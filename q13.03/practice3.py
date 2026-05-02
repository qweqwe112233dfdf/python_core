try:
    grades = input('введіть через пробіл оцінки студентів: ')
    numbers = list(map(int, grades.split()))
    average = sum(numbers) / len(numbers) 
    print('середня оцінка: ',average)
except ValueError:
    print('pomylka')
except ZeroDivisionError:
    print('список не може бути порожнім')
finally:
    print('завершення обчислень')