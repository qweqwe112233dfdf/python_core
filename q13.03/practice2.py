while(True):
    try:
        dollars = float(input('введіть суму в доларах: '))
        euro_kurs = float(input('введіть курс обміну на євро: '))
        euro = dollars / euro_kurs
        if euro_kurs == 0:
            raise Exception('курс обміну не може дорівнювати нулю')        
        print('сума в євро:', euro)
    except ValueError:
        print('помилка')
    finally:
        repeat = input('continue? Y/N')
        if repeat.lower() == 'n':
            break