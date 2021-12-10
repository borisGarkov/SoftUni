def case_shoot(targets_list, action, index, power):
    if 0 <= index < len(targets_list):
        targets_list[index] -= power
        if targets_list[index] <= 0:
            targets_list.pop(index)


def case_add(targets_list, action, index, value):
    if 0 <= index < len(targets_list):
        targets_list.insert(index, value)
    else:
        print("Invalid placement!")


def case_strike(targets_list, action, index, radius):
    start = index - radius
    end = index + radius + 1

    if start >= 0 and end <= len(targets_list):
        targets_list[:] = targets_list[:start] + targets_list[end:]
    else:
        print("Strike missed!")


targets_sequence = [int(target) for target in input().split()]

while True:
    command = input()

    if command == "End":
        break

    command = command.split()
    action = command[0]
    index = int(command[1])
    power = int(command[2])

    if action == "Shoot":
        case_shoot(targets_sequence, action, index, power)
    elif action == "Add":
        case_add(targets_sequence, action, index, power)
    elif action == "Strike":
        case_strike(targets_sequence, action, index, power)

print(*targets_sequence, sep="|")
