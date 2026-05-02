def draw_line(length, direction, symbol):
    if direction == "h":
        print(symbol * length)
    elif direction == "v":
        for _ in range(length):
            print(symbol)

draw_line(5, "h", "*")
draw_line(5, "v", "#")