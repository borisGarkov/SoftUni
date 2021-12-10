import sys


def exchange_lists(input_list, command):
    manipulator = command[0]
    index = int(command[1])

    if not (0 <= index < len(input_list)):
        print("Invalid index")
    else:
        first_half = input_list[:index + 1]
        second_half = input_list[index + 1:]

        joint_list = second_half + first_half
        input_list.clear()
        for element in joint_list:
            input_list.append(element)


def find_greatest_even_number(input_list, command):
    greatest_number = -sys.maxsize
    index_needed = None
    for num in range(len(input_list)):
        number = input_list[num]
        if number >= greatest_number and number % 2 == 0:
            greatest_number = number
            index_needed = num

    if index_needed == None:
        print("No matches")
    else:
        print(index_needed)


def find_greatest_odd_number(input_list, command):
    greatest_number = -sys.maxsize
    index_needed = None
    for num in range(len(input_list)):
        number = input_list[num]
        if number >= greatest_number and number % 2 != 0:
            greatest_number = number
            index_needed = num

    if index_needed == None:
        print("No matches")
    else:
        print(index_needed)


def find_smallest_even_number(input_list, command):
    smallest_number = sys.maxsize
    index_needed = None
    for num in range(len(input_list)):
        number = input_list[num]
        if number <= smallest_number and number % 2 == 0:
            smallest_number = number
            index_needed = num

    if index_needed == None:
        print("No matches")
    else:
        print(index_needed)


def find_smallest_odd_number(input_list, command):
    smallest_number = sys.maxsize
    index_needed = None
    for num in range(len(input_list)):
        number = input_list[num]
        if number <= smallest_number and number % 2 != 0:
            smallest_number = number
            index_needed = num

    if index_needed == None:
        print("No matches")
    else:
        print(index_needed)


def return_first_element(input_list, command):
    if int(command[1]) > len(input_list):
        print("Invalid count")
    else:
        count = int(command[1])
        return_list = []
        for num in range(count):
            number = input_list[num]
            if command[2] == "even" and number % 2 == 0:
                return_list.append(number)
            elif command[2] == "odd" and number % 2 != 0:
                return_list.append(number)
        print(return_list)


def return_last_element(input_list, command):
    if int(command[1]) > len(input_list):
        print("Invalid count")
    else:
        count = int(command[1])
        return_list = []
        for num in range(count - 1, -1, -1):
            number = input_list[num]
            if command[2] == "even" and number % 2 == 0:
                return_list.append(number)
            elif command[2] == "odd" and number % 2 != 0:
                return_list.append(number)
        print(return_list)


input_list = input().split()
numbers = list(map(int, input_list))

while True:
    command = input()
    if command == "end":
        break

    command = command.split(" ")
    if command[0] == "exchange":
        exchange_lists(numbers, command)

    elif command[0] == "max" and command[1] == "even":
        find_greatest_even_number(numbers, command)
    elif command[0] == "max" and command[1] == "odd":
        find_greatest_odd_number(numbers, command)
    elif command[0] == "min" and command[1] == "even":
        find_smallest_even_number(numbers, command)
    elif command[0] == "min" and command[1] == "odd":
        find_smallest_even_number(numbers, command)

    elif command[0] == "first":
        return_first_element(numbers, command)
    elif command[0] == "last":
        return_last_element(numbers, command)

print(numbers)
