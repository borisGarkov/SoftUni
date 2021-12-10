numbers_sequence = [int(number) for number in input().split()]
targets_shot = 0

while True:
    command = input()
    if command == "End":
        break

    index = int(command)
    if index in range(len(numbers_sequence)):
        current_target = numbers_sequence[index]
        if current_target == -1:
            continue
        for element in range(len(numbers_sequence)):
            if element == index or numbers_sequence[element] == -1:
                continue
            if numbers_sequence[element] > current_target:
                numbers_sequence[element] -= current_target
            else:
                numbers_sequence[element] += current_target
        numbers_sequence[index] = -1
        targets_shot += 1

print(f"Shot targets: {targets_shot} -> {' '.join([str(element) for element in numbers_sequence])}")