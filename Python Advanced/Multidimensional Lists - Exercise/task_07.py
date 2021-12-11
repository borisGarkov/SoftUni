def read_matrix():
    matrix_size = int(input())
    matrix = []
    for _ in range(matrix_size):
        matrix.append([int(el) for el in input().split()])

    bombs_coords = input().split()
    return matrix, bombs_coords


def is_coordinates_valid(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def is_cell_dead(matrix, row, col):
    if matrix[row][col] <= 0:
        return True
    return False


def get_bomb_explode(matrix, row, col):
    rows_data = [-1, 1, 0, 0, -1, -1, 1, 1]
    cols_data = [0, 0, -1, 1, -1, 1, -1, 1]

    for iteration in range(len(rows_data)):
        bomb_value = matrix[row][col]
        potential_row = rows_data[iteration] + row
        potential_col = cols_data[iteration] + col
        if is_coordinates_valid(matrix, potential_row, potential_col) and \
                not is_cell_dead(matrix, potential_row, potential_col):
            matrix[potential_row][potential_col] -= bomb_value

    matrix[row][col] = 0
    return matrix


def print_matrix(matrix):
    for row in range(len(matrix)):
        print_data = []
        for col in range(len(matrix)):
            print_data.append(str(matrix[row][col]))
        print(" ".join(print_data))


def main(matrix, bombs):
    for i in range(len(bombs)):
        row, col = [int(el) for el in bombs[i].split(",")]
        if not is_cell_dead(matrix, row, col):
            matrix = get_bomb_explode(matrix, row, col)

    alive_cells_count = 0
    the_sum = 0
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] > 0:
                alive_cells_count += 1
                the_sum += matrix[r][c]

    print(f"Alive cells: {alive_cells_count}")
    print(f"Sum: {the_sum}")
    print_matrix(matrix)


matrix, bombs = read_matrix()
main(matrix, bombs)
