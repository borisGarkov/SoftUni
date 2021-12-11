def is_move_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def check_for_letter(matrix, letter):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == letter:
                return row, col


def print_results(matrix, food_quantity):
    print(f"Food eaten: {food_quantity}")
    for row in range(len(matrix)):
        row_list = []
        for col in range(len(matrix)):
            row_list.append(matrix[row][col])
        print(*row_list, sep="")


MOVES = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

size = int(input())
food_quantity = 0
matrix = []
for _ in range(size):
    matrix.append([el for el in input()])

get_player_position = [row for row in matrix if "S" in row][0]
start_col = get_player_position.index("S")
start_row = matrix.index(get_player_position)
current_col = start_col
current_row = start_row

command = input()
while command != "":
    move_row, move_col = MOVES[command]
    potential_row = move_row + current_row
    potential_col = move_col + current_col

    if is_move_valid(matrix, potential_row, potential_col):
        if matrix[potential_row][potential_col] == "*":
            food_quantity += 1

        if matrix[potential_row][potential_col] == "B":
            matrix[potential_row][potential_col] = "."
            potential_row, potential_col = check_for_letter(matrix, "B")

        matrix[potential_row][potential_col] = "S"
        matrix[current_row][current_col] = "."

        current_row = potential_row
        current_col = potential_col
    else:
        matrix[current_row][current_col] = "."
        print("Game over!")
        print_results(matrix, food_quantity)
        break

    if food_quantity == 10:
        print("You won! You fed the snake.")
        print_results(matrix, food_quantity)
        break

    command = input()
