def read_matrix():
    row, col = [int(el) for el in input().split()]
    matrix = []
    for _ in range(row):
        matrix.append([el for el in input().split()])
    return matrix


def get_coordinates(line_to_check):
    row_1, col_1, row_2, col_2 = [int(el) for el in line_to_check]
    return row_1, col_1, row_2, col_2


def are_coordinates_valid(matrix, line_to_check):
    if len(line_to_check) == 4:
        row_1, col_1, row_2, col_2 = get_coordinates(line_to_check)
        if row_1 in range(len(matrix)) and col_1 in range(len(matrix[0])) and \
                row_2 in range(len(matrix)) and col_2 in range(len(matrix[0])):
            return True
    print("Invalid input!")
    return False


def print_matrix(matrix):
    for row in range(len(matrix)):
        submatrix = []
        for col in range(len(matrix[row])):
            submatrix.append(matrix[row][col])
        print(" ".join([str(el) for el in submatrix]))


def commands_read(matrix):
    while True:
        command = input().split()
        if command[0] == "END":
            break

        if are_coordinates_valid(matrix, command[1:]) and command[0] == "swap":
            row_1, col_1, row_2, col_2 = get_coordinates(command[1:])
            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            print_matrix(matrix)


matrix = read_matrix()
commands_read(matrix)
