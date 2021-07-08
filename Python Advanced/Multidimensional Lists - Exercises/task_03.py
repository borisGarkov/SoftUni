def read_matrix():
    n, m = [int(el) for el in input().split()]
    matrix = []
    for _ in range(n):
        matrix.append([int(el) for el in input().split()])
    return matrix


def find_best_matrix_sum(matrix, row_index, col_index, submatrix_size):
    the_sum = 0
    for r in range(row_index, row_index + submatrix_size):
        for c in range(col_index, col_index + submatrix_size):
            the_sum += matrix[r][c]
    return the_sum


def get_best_index(matrix, submatrix_size):
    best_row_index = 0
    best_col_index = 0
    best_sum = 0
    for r in range(len(matrix) - submatrix_size + 1):
        for c in range(len(matrix[r]) - submatrix_size + 1):
            current_sum = find_best_matrix_sum(matrix, r, c, submatrix_size)
            if current_sum > best_sum:
                best_sum = current_sum
                best_row_index = r
                best_col_index = c
    return best_row_index, best_col_index, best_sum


def print_results(matrix, submatrix_size):
    row, col, sum = get_best_index(matrix, submatrix_size)
    print(f"Sum = {sum}")
    for r in range(row, row + submatrix_size):
        row = []
        for c in range(col, col + submatrix_size):
            row.append(matrix[r][c])
        print(" ".join([str(el) for el in row]))


matrix = read_matrix()
submatrix_size = 3
print_results(matrix, submatrix_size)
