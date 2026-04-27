import random

def connect_to_server():
    if random.choice([True, False]):
        return "Підключено!"
    else:
        raise ConnectionError("Помилка підключення")

try:
    print(connect_to_server())
except ConnectionError:
    print("Не вдалося підключитися до сервера")
finally:
    print("Спробу завершено")