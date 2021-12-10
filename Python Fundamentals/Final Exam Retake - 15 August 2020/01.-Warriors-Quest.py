string = input()
while True:
    command_data = input().split()
    command = command_data[0]
    if command == "For" and command_data[1] == "Azeroth":
        break

    if command == "GladiatorStance":
        string = string.upper()
        print(string)
    elif command == "DefensiveStance":
        string = string.lower()
        print(string)
    elif command == "Dispel":
        index, letter = command_data[1:]
        index = int(index)
        if index in range(0, len(string)):
            string = string[:index] + letter + string[index + 1:]
            print("Success!")
        else:
            print("Dispel too weak.")
    elif command == "Target" and command_data[1] == "Change":
        substring, replacement = command_data[2:]
        string = string.replace(substring, replacement)
        print(string)
    elif command == "Target" and command_data[1] == "Remove":
        substring = command_data[2]
        string = string.replace(substring, "")
        print(string)
    else:
        print("Command doesn't exist!")