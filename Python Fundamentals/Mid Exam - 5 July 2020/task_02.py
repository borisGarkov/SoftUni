numbers_list = [int(number) for number in input().split()]


def swap(numbers_list, index_1, index_2):
    numbers_list[index_1], numbers_list[index_2] = numbers_list[index_2], numbers_list[index_1]
    return numbers_list


def multiply(numbers_list, index_1, index_2):
    numbers_list[index_1] = numbers_list[index_1] * numbers_list[index_2]
    return numbers_list


def decrease(numbers_list):
    numbers_list[:] = [number - 1 for number in numbers_list]
    return numbers_list


while True:
    command = input()
    if command == "end":
        break

    if command == "decrease":
        decrease(numbers_list)
        continue

    action, index_1, index_2 = command.split()
    index_1 = int(index_1)
    index_2 = int(index_2)

    if action == "swap":
        swap(numbers_list, index_1, index_2)
    elif action == "multiply":
        multiply(numbers_list, index_1, index_2)

print(*numbers_list, sep=", ")
