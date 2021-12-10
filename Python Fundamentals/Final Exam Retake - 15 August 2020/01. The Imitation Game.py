message = input()

while True:
    command_data = input().split("|")
    command = command_data[0]
    if command == "Decode":
        break

    if command == "Move":
        n_letters = int(command_data[1])
        message = message[n_letters:] + message[:n_letters]
    elif command == "Insert":
        index, value = command_data[1:]
        index = int(index)
        message = list(message)
        message.insert(index, value)
        message = "".join([str(element) for element in message])
    elif command == "ChangeAll":
        substring, replacement = command_data[1:]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
