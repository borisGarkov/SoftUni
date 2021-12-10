numbers_collection = [int(number) for number in input().split()]

while True:
    data = input()
    if data == "END":
        break

    if data == "Reverse":
        numbers_collection = numbers_collection[::-1]
    elif data.split()[0] == "Hide":
        painting_number = data.split()[1]
        painting_number = int(painting_number)
        if painting_number in numbers_collection:
            numbers_collection.remove(painting_number)
    else:
        command, first_element, second_element = data.split()
        first_element = int(first_element)
        second_element = int(second_element)

        if command == "Change":
            if first_element in numbers_collection:
                index = numbers_collection.index(first_element)
                numbers_collection[index] = second_element
        elif command == "Switch":
            if first_element in numbers_collection and second_element in numbers_collection:
                index_1 = numbers_collection.index(first_element)
                index_2 = numbers_collection.index(second_element)

                numbers_collection[index_1], numbers_collection[index_2] = \
                    numbers_collection[index_2], numbers_collection[index_1]

        elif command == "Insert":
            if first_element + 1 in range(len(numbers_collection)):
                numbers_collection.insert(first_element + 1, second_element)

print(*numbers_collection)
