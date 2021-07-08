def read_matrix():
    matrix_length = int(input())
    matrix = []
    for _ in range(matrix_length):
        matrix.append([int(el) for el in input().split()])
    return matrix


def find_primary_diagonal_sum(matrix):
    the_sum = 0
    for row_index in range(len(matrix)):
        for col_index in range(row_index, row_index + 1):
            the_sum += matrix[row_index][col_index]
    return the_sum


def find_secondary_diagonal_sum(matrix):
    the_sum = 0
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix) - row_index - 1, len(matrix) - row_index - 2, -1):
            the_sum += matrix[row_index][col_index]
    return the_sum


matrix = read_matrix()
result_primary_diagonal_sum = find_primary_diagonal_sum(matrix)
result_secondary_diagonal_sum = find_secondary_diagonal_sum(matrix)
print(abs(result_primary_diagonal_sum - result_secondary_diagonal_sum))
