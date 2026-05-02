rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}

currency = input("Валюта (USD/EUR/PLN): ")
uah = float(input("Сума в грн: "))

if currency in rates:
    print("Сума:", uah / rates[currency])
else:
    print("Невідома валюта")