username = input()

while True:
    command_data = input().split()
    command = command_data[0]
    if command == "Sign":
        break

    if command == "Case":
        case = command_data[1]
        if case == "lower":
            username = username.lower()
        else:
            username = username.upper()
        print(username)
    elif command == "Reverse":
        start, end = command_data[1:]
        start = int(start)
        end = int(end)
        if start in range(0, len(username)) and end in range(0, len(username)):
            temp = username[start:end + 1]
            temp = temp[::-1]
            print(temp)
    elif command == "Cut":
        substring = command_data[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")
    elif command == "Replace":
        char = command_data[1]
        username = username.replace(char, "*")
        print(username)
    elif command == "Check":
        char = command_data[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
