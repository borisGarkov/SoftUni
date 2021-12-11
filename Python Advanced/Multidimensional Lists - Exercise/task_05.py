from collections import deque


def read_matrix():
    row_value, col_value = [int(el) for el in input().split()]
    string_input = deque(input())
    matrix = [[0 for i in range(col_value)] for el in range(row_value)]
    return matrix, string_input


def move_snake(matrix, snake):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] = snake[0]
            snake.append(snake.popleft())
        if row % 2 == 0:
            print("".join(matrix[row]))
        else:
            print("".join(matrix[row][::-1]))


matrix, snake = read_matrix()
move_snake(matrix, snake)
