gifts_list = input().split(" ")

while True:
    command = input()
    command_list = []

    if command == "No Money":
        for _ in gifts_list:
            if "None" in gifts_list:
                gifts_list.remove("None")

        print(*gifts_list)
        break
    else:
        command_list = command.split(" ")

    if command_list[0] == "OutOfStock":
        for index in range(len(gifts_list)):
            if command_list[1] == gifts_list[index]:
                gifts_list[index] = "None"

    elif command_list[0] == "Required":
        if int(command_list[2]) in range(len(gifts_list)):
            gifts_list[int(command_list[2])] = command_list[1]

    elif command_list[0] == "JustInCase":
        gifts_list[-1] = command_list[1]


