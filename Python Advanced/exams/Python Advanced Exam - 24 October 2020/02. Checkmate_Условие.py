matrix = []


def is_coord_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def move_queens(matrix, current_row, current_col):
    row_data = [-1, 1, 0, 0, -1, -1, 1, 1]
    col_data = [0, 0, -1, 1, -1, 1, -1, 1]

    for index in range(len(row_data)):
        potential_row = current_row + row_data[index]
        potential_col = current_col + col_data[index]
        while True:
            if is_coord_valid(matrix, potential_row, potential_col):
                if matrix[potential_row][potential_col] == "Q":
                    break
                elif matrix[potential_row][potential_col] == "K":
                    return True
                else:
                    potential_row += row_data[index]
                    potential_col += col_data[index]
            else:
                break
    return False


for _ in range(8):
    matrix.append([el for el in input().split()])

is_king_safe = True
for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == "Q":
            if move_queens(matrix, row, col):
                print(f"[{row}, {col}]")
                is_king_safe = False

if is_king_safe:
    print("The king is safe!")