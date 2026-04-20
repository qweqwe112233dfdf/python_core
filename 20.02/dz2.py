try:
    count = int(input("Скільки всього гравців (ви + друзі)? "))
    
    all_games_sets = []

    for i in range(count):
        games_input = input(f"Введіть ігри гравця {i+1} через кому: ")
        games_set = {game.strip().lower() for game in games_input.split(",")}
        all_games_sets.append(games_set)

    if all_games_sets:
        common_games = set.intersection(*all_games_sets)

        if common_games:
            print("\nІгри, в які можуть зіграти всі разом:")
            print(", ".join(common_games))
        else:
            print("\nНа жаль, спільних ігор для всіх немає.")
            
except ValueError:
    print("Будь ласка, введіть коректне число.")