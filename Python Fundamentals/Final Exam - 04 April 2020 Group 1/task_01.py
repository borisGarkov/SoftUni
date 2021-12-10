activation_key = input()


def case_contains(substring, string):
    if substring in string:
        return f"{string} contains {substring}"
    return "Substring not found!"


def case_flip(switch_case, start_index, end_index, string):
    if switch_case == "Upper":
        string_to_upper = string[:start_index] + string[start_index:end_index].upper() + string[end_index:]
        return string_to_upper
    string_to_lower = string[:start_index] + string[start_index:end_index].lower() + string[end_index:]
    return string_to_lower


def case_slice(start_index, end_index, string):
    string_to_return = string[:start_index] + string[end_index:]
    return string_to_return


while True:
    command = input()
    if command == "Generate":
        break

    if command.split(">>>")[0] == "Contains":
        _, substring = command.split(">>>")
        print(case_contains(substring, activation_key))
    elif command.split(">>>")[0] == "Flip":
        _, switch_case, start_index, end_index = command.split(">>>")
        start_index = int(start_index)
        end_index = int(end_index)
        activation_key = case_flip(switch_case, start_index, end_index, activation_key)
        print(activation_key)
    elif command.split(">>>")[0] == "Slice":
        _, start_index, end_index = command.split(">>>")
        start_index = int(start_index)
        end_index = int(end_index)
        activation_key = case_slice(start_index, end_index, activation_key)
        print(activation_key)

print(f"Your activation key is: {activation_key}")
