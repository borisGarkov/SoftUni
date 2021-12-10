def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(sum_function_result, num_3):
    return sum_function_result - num_3


def add_and_subtract():
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())

    print(subtract(sum_numbers(num_1, num_2), num_3))


add_and_subtract()
