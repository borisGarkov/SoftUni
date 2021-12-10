line = input()

while True:
    command_data = input().split()
    command = command_data[0]
    if command == "Travel":
        break

    if command == "Add":
        _, index, string = command_data[1].split(":")
        index = int(index)

        if index in range(len(line)):
            line = list(line)
            line.insert(index, string)
            line = "".join(element for element in line)
        print(line)

    elif command == "Remove":
        _, start, end = command_data[1].split(":")
        start = int(start)
        end = int(end)

        if start in range(len(line)) and end in range(len(line)):
            line = line[:start] + line[end + 1:]
        print(line)
    else:
        _, old, new = command_data[0].split(":")
        if old in line:
            line = line.replace(old, new)
        print(line)

print(f"Ready for world tour! Planned stops: {line}")
