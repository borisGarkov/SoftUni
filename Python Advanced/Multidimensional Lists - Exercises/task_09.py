from copy import deepcopy

possible_moves = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1]
}


def check_if_coords_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        return True
    return False


def print_matrix(matrix):
    print("\n".join(["".join(el) for el in matrix]))


def move_rabbits(matrix):
    rows_data = [-1, 1, 0, 0]
    cols_data = [0, 0, -1, 1]
    matrix_copy = deepcopy(matrix)
    is_player_found = False
    final_row = 0
    final_col = 0

    for row in range(len(matrix_copy)):
        for col in range(len(matrix_copy[row])):
            if matrix_copy[row][col] == "B":

                for r in range(len(rows_data)):
                    next_row = row + rows_data[r]
                    next_col = col + cols_data[r]
                    if check_if_coords_valid(matrix, next_row, next_col):
                        if matrix[next_row][next_col] == "." or matrix[next_row][next_col] == "B":
                            matrix[next_row][next_col] = "B"
                        else:
                            matrix[next_row][next_col] = "B"
                            final_row = next_row
                            final_col = next_col
                            is_player_found = True

    if is_player_found:
        print_matrix(matrix)
        print(f"dead: {final_row} {final_col}")
        exit()
    return matrix


data = input().split()
rows = int(data[0])
cols = int(data[1])
matrix = []

for _ in range(rows):
    matrix.append([el for el in input()])

directions = input()

player_position_row = 0
player_position_col = 0
is_player_found = False
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "P":
            player_position_row = row
            player_position_col = col
            is_player_found = True
            break
    if is_player_found:
        break

for d in directions:
    row, col = possible_moves[d]
    next_row = row + player_position_row
    next_col = col + player_position_col
    if check_if_coords_valid(matrix, next_row, next_col):

        matrix[next_row][next_col] = "P"
        matrix[player_position_row][player_position_col] = "."
        player_position_row = next_row
        player_position_col = next_col

        matrix = move_rabbits(matrix)
    else:
        matrix[player_position_row][player_position_col] = "."
        matrix = move_rabbits(matrix)
        print_matrix(matrix)
        print(f"won: {player_position_row} {player_position_col}")
        break
