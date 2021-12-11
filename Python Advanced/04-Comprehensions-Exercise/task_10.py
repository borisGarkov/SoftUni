row = int(input())
matrix = [[int(col) for col in input().split()] for el in range(row)]


def is_coords_valid(matrix, row, col):
    if row in range(len(matrix)) and col in range(len(matrix)):
        return True
    return False


def case_add(matrix, row, col, value):
    if is_coords_valid(matrix, row, col):
        matrix[row][col] += value
    else:
        print("Invalid coordinates")
    return matrix


def case_subtract(matrix, row, col, value):
    if is_coords_valid(matrix, row, col):
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    return matrix


while True:
    line = input()
    if line == "END":
        break
    action, row, col, value = line.split()
    row = int(row)
    col = int(col)
    value = int(value)
    if action == "Add":
        matrix = case_add(matrix, row, col, value)
    else:
        matrix = case_subtract(matrix, row, col, value)

print('\n'.join([' '.join([str(matrix[r][c]) for c in range(len(matrix))]) for r in range(len(matrix))]))
