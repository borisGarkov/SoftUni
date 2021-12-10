sugar_cubes = [int(number) for number in input().split()]


def case_add(sugar_cubes, value):
    sugar_cubes.append(value)
    return sugar_cubes


def case_remove(sugar_cubes, value):
    if value in sugar_cubes:
        sugar_cubes.remove(value)
    return sugar_cubes


def case_collapse(sugar_cubes, value):
    sugar_cubes = [element for element in sugar_cubes if element >= value]
    return sugar_cubes


while True:
    command = input()
    if command == "Mort":
        print(*sugar_cubes)
        break

    if command.split()[0] == "Replace":
        command, value, replacement = command.split()
        value = int(value)
        replacement = int(replacement)

        index = sugar_cubes.index(value)
        sugar_cubes[index] = replacement

    else:
        command, value = command.split()
        value = int(value)

        if command == "Add":
            sugar_cubes = case_add(sugar_cubes, value)
        elif command == "Remove":
            sugar_cubes = case_remove(sugar_cubes, value)
        elif command == "Collapse":
            sugar_cubes = case_collapse(sugar_cubes, value)
