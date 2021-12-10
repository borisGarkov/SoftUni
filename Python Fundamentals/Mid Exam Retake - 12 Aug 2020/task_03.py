sequence = input().split()
number_of_moves_till_now = 0


def are_indexes_same(a, b, sequence_list):
    if a > b:
        greater_index = a
        minor_index = b
    else:
        greater_index = b
        minor_index = a

    result = sequence_list[greater_index]
    sequence_list.pop(greater_index)
    sequence_list.pop(minor_index)
    return f"Congrats! You have found matching elements - {result}!"


def insert_element_at_index(number_of_moves_till_now, sequence_list):
    average = len(sequence_list) // 2
    sequence_list.insert(average, "-" + str(number_of_moves_till_now) + "a")
    sequence_list.insert(average + 1, "-" + str(number_of_moves_till_now) + "a")
    return "Invalid input! Adding additional elements to the board"


while True:
    command = input()
    if command == "end":
        break

    number_of_moves_till_now += 1
    index_1, index_2 = [int(number) for number in command.split()]

    if index_1 == index_2 or index_1 not in range(len(sequence)) or index_2 not in range(len(sequence)):
        print(insert_element_at_index(number_of_moves_till_now, sequence))
    elif sequence[index_1] == sequence[index_2] and 0 <= index_1 < len(sequence) and 0 <= index_2 < len(sequence):
        print(are_indexes_same(index_1, index_2, sequence))
    else:
        print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {number_of_moves_till_now} turns!")
        break

if len(sequence) > 0:
    print("Sorry you lose :(")
    print(f"{' '.join(sequence)}")
