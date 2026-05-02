try:
    price = float(input('введіть початкову ціну: '))
    discount = float(input('введіть відсоток знижки: '))
    final_price = price * (discount / 100)
    print('фінальна ціна товару:', final_price)
except ValueError:
    print('помилка!')