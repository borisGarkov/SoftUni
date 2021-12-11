import math

size = int(input())
matrix = []
path = []
coins = 0

moves = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}


def check_if_coords_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def player_lost(coins, path):
    coins = coins / 2
    math.floor(coins)
    coins = int(coins)
    print(f"Game over! You've collected {coins} coins.")
    print_path(path)
    exit()


def print_path(path):
    print("Your path:")
    for p in path:
        print(p)


initial_row = 0
initial_col = 0
for r in range(size):
    line = input().split()
    if "P" in line:
        initial_row = r
        initial_col = line.index("P")
    matrix.append(line)

command = input()
while not command == "":
    next_row, next_col = moves[command]
    potential_row = initial_row + next_row
    potential_col = initial_col + next_col

    if check_if_coords_valid(matrix, potential_row, potential_col):
        if matrix[potential_row][potential_col].isnumeric():
            coins += int(matrix[potential_row][potential_col])
        elif matrix[potential_row][potential_col] == "X":
            player_lost(coins, path)
    else:
        player_lost(coins, path)

    initial_row = potential_row
    initial_col = potential_col

    path.append([potential_row, potential_col])
    if coins >= 100:
        print(f"You won! You've collected {coins:.0f} coins.")
        print_path(path)
        break

    command = input()
