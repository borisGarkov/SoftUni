targets = [int(number) for number in input().split()]


def case_shoot(targets, index, power):
    if index in range(len(targets)):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    return targets


def case_add(targets, index, value):
    if index in range(len(targets)):
        targets.insert(index, value)
    else:
        print("Invalid placement!")
    return targets


def case_strike(targets, index, radius):
    if index + radius in range(len(targets)) and index - radius in range(len(targets)):
        start = index - radius
        end = index + radius
        targets = targets[:start] + targets[end + 1:]
    else:
        print("Strike missed!")
    return targets


while True:
    command = input()
    if command == "End":
        break

    action, index, value = command.split()
    index = int(index)
    value = int(value)

    if action == "Shoot":
        targets = case_shoot(targets, index, value)
    elif action == "Add":
        targets = case_add(targets, index, value)
    elif action == "Strike":
        targets = case_strike(targets, index, value)

print("|".join([str(number) for number in targets]))
