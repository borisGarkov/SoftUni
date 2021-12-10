def find_closest_points(x_1, y_1, x_2, y_2):
    result_1 = int(abs(x_1) + abs(y_1))
    result_2 = int(abs(x_2) + abs(y_2))

    if result_1 <= result_2:
        print(f"({int(x_1)}, {int(y_1)})")
    else:
        print(f"({int(x_2)}, {int(y_2)})")

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

find_closest_points(x_1, y_1, x_2, y_2)
