def insert_space(message, index):
    message = list(message)
    message.insert(index, ' ')
    result = "".join(str(element) for element in message)
    print(result)
    return result


def reverse(message, substring):
    if substring in message:
        message = message.replace(substring, '', 1)
        message += substring[::-1]
        print(message)
    else:
        print("error")
    return message


def replace_sub(message, substring, replacement):
    message = message.replace(substring, replacement)
    print(message)
    return message


concealed_message = input()

while True:
    command_data = input().split(":|:")
    command = command_data[0]
    if command == "Reveal":
        break

    if command == "InsertSpace":
        index = int(command_data[1])
        concealed_message = insert_space(concealed_message, index)
    elif command == "Reverse":
        substring = command_data[1]
        concealed_message = reverse(concealed_message, substring)
    elif command == "ChangeAll":
        substring, replacement = command_data[1:]
        concealed_message = replace_sub(concealed_message, substring, replacement)

print(f"You have a new text message: {concealed_message}")
