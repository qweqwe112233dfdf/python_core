def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    days = [31, 28 + is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month - 1]

def date_to_days(days, m, y):
    for year in range(1, y):
        days += 366 if is_leap(year) else 365
    for month in range(1, m):
        days += days_in_month(month, y)
    return days

def date_diff(d1, m1, y1, d2, m2, y2):
    return abs(date_to_days(d1, m1, y1) - date_to_days(d2, m2, y2))

print(date_diff(1, 1, 2023, 1, 1, 2024))