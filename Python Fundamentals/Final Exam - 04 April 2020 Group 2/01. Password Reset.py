string = input()


def take_odd(string):
    string_to_return = ""
    for index in range(len(string)):
        if not index % 2 == 0:
            string_to_return += string[index]
    return string_to_return


def cut(string, index, length):
    string_to_return = string[:index] + string[index + length:]
    return string_to_return


def case_substitute(string, substring, substitute):
    if substring in string:
        string_to_return = string.replace(substring, substitute)
        print(string_to_return)
        return string_to_return
    print("Nothing to replace!")
    return string


while True:
    command = input()
    if command == "Done":
        print(f"Your password is: {string}")
        break

    if command == "TakeOdd":
        string = take_odd(string)
        print(string)
    elif command.split()[0] == "Cut":
        _, index, length = command.split()
        index = int(index)
        length = int(length)
        string = cut(string, index, length)
        print(string)
    elif command.split()[0] == "Substitute":
        _, substring, substitute = command.split()
        string = case_substitute(string, substring, substitute)


