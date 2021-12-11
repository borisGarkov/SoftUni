def list_manipulator(list_numbers, *data):
    data = list(data)
    command, location = data[:2]
    if len(data) > 2:
        numbers_to_manipulate = data[2:]

        if command == "add" and location == "beginning":
            list_numbers = numbers_to_manipulate + list_numbers
        elif command == "add" and location == "end":
            list_numbers += numbers_to_manipulate
        elif command == "remove" and location == "beginning":
            index = data[2]
            list_numbers = list_numbers[index:]
            return list_numbers
        elif command == "remove" and location == "end":
            index = data[2]
            list_numbers = list_numbers[:-index]
            return list_numbers

    if command == "remove" and location == "beginning":
        list_numbers = list_numbers[1:]
    elif command == "remove" and location == "end":
        list_numbers = list_numbers[:-1]

    return list_numbers


# print(list_manipulator([1, 2, 3], "remove", "end"))
# print(list_manipulator([1, 2, 3], "remove", "beginning"))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20))
# print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
# print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
# print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
# print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
