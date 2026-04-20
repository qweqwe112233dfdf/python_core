def draw_square(side, symbol, filled):
    for i in range(side):
        for j in range(side):
            if filled or i == 0 or i == side - 1 or j == 0 or j == side - 1:
                print(symbol, end=" ")
            else:
                print(" ", end=" ")
        print()

draw_square(5, "*", True)
print("---")
draw_square(5, "#", False)