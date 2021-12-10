def check_coordinates(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    first_line = abs(x_1) + abs(y_1) + abs(x_2) + abs(y_2)
    second_line = abs(x_3) + abs(y_3) + abs(x_4) + abs(y_4)
    if first_line >= second_line:
        if abs(x_1) + abs(y_1) > abs(x_2) + abs(y_2):
            print(f"({int(x_2)}, {int(y_2)})({int(x_1)}, {int(y_1)})")
        else:
            print(f"({int(x_1)}, {int(y_1)})({int(x_2)}, {int(y_2)})")
    else:
        if abs(x_3) + abs(y_3) > abs(x_4) + abs(y_4):
            print(f"({int(x_4)}, {int(y_4)})({int(x_3)}, {int(y_3)})")
        else:
            print(f"({int(x_3)}, {int(y_3)})({int(x_4)}, {int(y_4)})")


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())

check_coordinates(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4)
