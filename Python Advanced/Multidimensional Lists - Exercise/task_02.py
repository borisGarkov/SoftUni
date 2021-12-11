def read_matrix():
    rows_count, cols_count = [int(el) for el in input().split()]
    matrix = []
    for _ in range(rows_count):
        matrix.append([el for el in input().split()])
    return matrix


def find_count_equal_char_matrices(matrix):
    counter = 0
    submatrix_size = 2
    for row_index in range(len(matrix) - submatrix_size + 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            first_index = matrix[row_index][col_index]
            second_index = matrix[row_index][col_index + 1]
            third_index = matrix[row_index + 1][col_index]
            forth_index = matrix[row_index + 1][col_index + 1]
            if first_index == second_index and first_index == third_index and first_index == forth_index:
                counter += 1
    return counter


matrix = read_matrix()
sum_equal_char_matrices = find_count_equal_char_matrices(matrix)
print(sum_equal_char_matrices)
