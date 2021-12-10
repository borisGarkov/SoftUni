targets = [int(number) for number in input().split("|")]
points = 0

while True:
    command = input()
    if command == "Game over":
        break

    data = command.split()
    if data[0] == "Shoot":
        direction, starting_index, length = data[1].split("@")
        starting_index = int(starting_index)
        length = int(length)

        if starting_index in range(len(targets)):
            if direction == "Left":
                index = (starting_index - length) % len(targets)
            else:
                index = (starting_index + length) % len(targets)

            if targets[index] < 5:
                points += targets[index]
                targets[index] = 0
            else:
                targets[index] -= 5
                points += 5

    elif data[0] == "Reverse":
        targets = targets[::-1]


print(" - ".join([str(number) for number in targets]))
print(f"Iskren finished the archery tournament with {points} points!")
