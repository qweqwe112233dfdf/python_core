from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import random

console = Console()

history = []
round_num = 1

choices_map = {
    "1": "Камінь",
    "2": "Ножиці",
    "3": "Папір"
}

def get_result(player, computer):
    if player == computer:
        return "Нічия"
    elif (
        (player == "1" and computer == "2") or
        (player == "2" and computer == "3") or
        (player == "3" and computer == "1")
    ):
        return "Перемога"
    else:
        return "Поразка"

def color_result(result):
    if result == "Перемога":
        return "[green]Перемога[/green]"
    elif result == "Поразка":
        return "[red]Поразка[/red]"
    else:
        return "[yellow]Нічия[/yellow]"

def play_game():
    global round_num

    player = Prompt.ask(
        "[bold yellow]Ваш вибір [1-Камінь, 2-Ножиці, 3-Папір][/bold yellow]",
        choices=["1", "2", "3"]
    )

    computer = str(random.randint(1, 3))

    console.print(f"Комп'ютер обрав: [cyan]{choices_map[computer]}[/cyan]")

    result = get_result(player, computer)

    console.print(f"Результат: {color_result(result)}", style="bold")

    history.append({
        "round": round_num,
        "player": choices_map[player],
        "computer": choices_map[computer],
        "result": result
    })

    round_num += 1

def show_history():
    if not history:
        console.print("[yellow]Історія порожня[/yellow]")
        return

    table = Table(title="Історія матчів")

    table.add_column("Раунд", justify="center")
    table.add_column("Гравець")
    table.add_column("Комп'ютер")
    table.add_column("Результат")

    wins = losses = draws = 0

    for game in history:
        if game["result"] == "Перемога":
            wins += 1
        elif game["result"] == "Поразка":
            losses += 1
        else:
            draws += 1

        table.add_row(
            str(game["round"]),
            game["player"],
            game["computer"],
            color_result(game["result"])
        )

    console.print(table)

    console.print(
        f"[bold]Статистика:[/bold] "
        f"[green]Перемоги: {wins}[/green], "
        f"[red]Поразки: {losses}[/red], "
        f"[yellow]Нічиї: {draws}[/yellow]"
    )

def main_menu():
    while True:
        console.clear()

        menu = Panel(
            "[bold cyan]1.[/bold cyan] Почати гру\n"
            "[bold cyan]2.[/bold cyan] Історія ігор\n"
            "[bold cyan]3.[/bold cyan] Вихід",
            title="[bold magenta]Головне меню[/bold magenta]",
            border_style="white"
        )

        console.print("[bold green]Вітаємо в Аркаді![/bold green]")
        console.print(menu)

        choice = Prompt.ask(
            "Оберіть дію",
            choices=["1", "2", "3"]
        )

        if choice == "1":
            play_game()
            console.input("\nНатисніть Enter")
        elif choice == "2":
            show_history()
            console.input("\nНатисніть Enter")
        elif choice == "3":
            break

main_menu()