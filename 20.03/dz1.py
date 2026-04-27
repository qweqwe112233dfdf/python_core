with open('data.txt', 'w') as file:
    for i in range(3):
        line = input(f"Введіть рядок {i+1}: ")
        file.write(line + '\n')

print("Дані успішно записані у data.txt")