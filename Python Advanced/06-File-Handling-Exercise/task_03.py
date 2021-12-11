import os


def command_create(file_name):
    with open(file_name, 'w') as file:
        pass


def command_add(file_name, file_text):
    if not os.path.exists(file_name):
        with open(file_name, "x") as file:
            file.write(file_text)
    else:
        with open(file_name, "a") as file:
            file.write(file_text + "\n")


def command_replace(file_name, old_string, new_string):
    try:
        with open(file_name, "r") as file:
            file_data = file.read()

        file_data = file_data.replace(old_string, new_string)
        with open(file_name, "w") as file:
            file.write(file_data)

    except FileNotFoundError:
        print("An error occurred")


def command_delete(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


while True:
    data = input()
    if data == "End":
        break

    command = data.split("-")[0]
    if command == "Create":
        name = data.split("-")[1]
        command_create(name)
    elif command == "Add":
        name, content = data.split("-")[1:]
        command_add(name, content)
    elif command == "Replace":
        file_name, old_string, new_string = data.split("-")[1:]
        command_replace(file_name, old_string, new_string)
    elif command == "Delete":
        name = data.split("-")[1]
        command_delete(name)