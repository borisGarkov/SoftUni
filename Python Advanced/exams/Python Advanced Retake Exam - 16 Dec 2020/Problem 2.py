MOVES = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}


def is_coords_valid(matrix, potential_row, potential_col):
    if 0 <= potential_row < len(matrix) and 0 <= potential_col < len(matrix):
        return True
    return False


initial_string = list(input())
size_square = int(input())

matrix = []
for _ in range(size_square):
    matrix.append([el for el in input()])

get_player_position = [row for row in matrix if "P" in row][0]
start_col = get_player_position.index("P")
start_row = matrix.index(get_player_position)
current_col = start_col
current_row = start_row

n_commands = int(input())
for _ in range(n_commands):
    command = input()
    move_row, move_col = MOVES[command]
    potential_row = current_row + move_row
    potential_col = current_col + move_col
    if is_coords_valid(matrix, potential_row, potential_col):
        if matrix[potential_row][potential_col].isalpha():
            initial_string.append(matrix[potential_row][potential_col])
        matrix[potential_row][potential_col] = "P"
        matrix[current_row][current_col] = "-"
        current_row = potential_row
        current_col = potential_col
    else:
        if initial_string:
            initial_string.pop()

print(*initial_string, sep="")
for row in range(len(matrix)):
    data = []
    for col in range(len(matrix)):
        data.append(matrix[row][col])
    print(*data, sep="")
