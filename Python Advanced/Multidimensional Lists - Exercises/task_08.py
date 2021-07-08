MOVES_DATA = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}


def read_matrix():
    size = int(input())
    commands = [el for el in input().split()]
    matrix = []
    for _ in range(size):
        matrix.append([el for el in input().split()])
    return matrix, commands


def is_valid_coordinates(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


def check_if_coals_left(matrix):
    coals_left = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col] == "c":
                coals_left += 1
    return coals_left


def move_miner(matrix, commands):
    coal_count = 0
    get_col = [row for row in matrix if "s" in row][0]
    start_col = get_col.index("s")
    start_row = matrix.index(get_col)
    current_col = start_col
    current_row = start_row
    for command in commands:
        move_row, move_col = MOVES_DATA[command]
        potential_row = move_row + current_row
        potential_col = move_col + current_col
        if is_valid_coordinates(matrix, potential_row, potential_col):
            if matrix[potential_row][potential_col] == "c":
                coal_count += 1
                matrix[potential_row][potential_col] = "*"
            elif matrix[potential_row][potential_col] == "e":
                print(f"Game over! ({potential_row}, {potential_col})")
                exit()
            current_row = potential_row
            current_col = potential_col
    coals_left = check_if_coals_left(matrix)
    if not coals_left:
        print(f"You collected all coals! ({potential_row}, {potential_col})")
    else:
        print(f"{coals_left} coals left. ({potential_row}, {potential_col})")


matrix, commands = read_matrix()
move_miner(matrix, commands)
