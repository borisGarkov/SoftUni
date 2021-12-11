size = int(input())
bomb_coords = int(input())
matrix = [[0 for i in range(size)] for el in range(size)]


def check_if_coords_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def count_surrounding_bombs(matrix, row, col):
    row_data = [-1, 1, 0, 0, -1, -1, 1, 1]
    col_data = [0, 0, -1, 1, -1, 1, -1, 1]

    for r in range(len(row_data)):
        next_row = row + row_data[r]
        next_col = col + col_data[r]
        if check_if_coords_valid(matrix, next_row, next_col):
            if matrix[next_row][next_col] == "*":
                matrix[row][col] += 1

    return matrix


for _ in range(bomb_coords):
    coords = input().split(", ")
    row = int(coords[0].replace("(", ""))
    col = int(coords[1].replace(")", ""))
    matrix[row][col] = "*"

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if not matrix[row][col] == "*":
            matrix = count_surrounding_bombs(matrix, row, col)


print("\n".join([" ".join(map(str, el)) for el in matrix]))
