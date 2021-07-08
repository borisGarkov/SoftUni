def read_matrix():
    size = int(input())
    matrix = []
    for row in range(size):
        line = input()
        matrix.append(list(line))
    return matrix


def is_coord_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def move_knight(matrix, current_row, current_col):
    row_data = [-2, -2, 2, 2, -1, 1, -1, 1]
    col_data = [-1, 1, -1, 1, -2, -2, 2, 2]

    n_kills = 0
    for value in range(len(row_data)):
        potential_row = current_row + row_data[value]
        potential_col = current_col + col_data[value]
        if is_coord_valid(matrix, potential_row, potential_col):
            if matrix[potential_row][potential_col] == "K":
                n_kills += 1
    return n_kills


def main(matrix):
    n_dead_knights = 0

    while True:
        biggest_killer = 0
        biggest_row = 0
        biggest_col = 0

        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if matrix[row][col] == "K":
                    kills_number = move_knight(matrix, row, col)
                    if kills_number > biggest_killer:
                        biggest_killer = kills_number
                        biggest_row = row
                        biggest_col = col

        if biggest_killer:
            n_dead_knights += 1
            matrix[biggest_row][biggest_col] = "0"
        else:
            break

    return n_dead_knights


matrix = read_matrix()
n_dead_knights = main(matrix)
print(n_dead_knights)
