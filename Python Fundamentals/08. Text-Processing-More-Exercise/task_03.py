keys = [int(number) for number in input().split()]
while True:
    string = input()
    if string == "find":
        break

    string = list(string)
    keys_index = 0
    for index in range(len(string)):
        if index >= len(keys):
            keys_index = index % len(keys)
        temp_ascii_code = ord(string[index])
        temp_ascii_code -= keys[keys_index]
        string[index] = chr(temp_ascii_code)
        keys_index += 1

    index = string.index("&") + 1
    treasure = ""
    while not string[index] == "&":
        treasure += string[index]
        index += 1

    start_index = string.index("<") + 1
    end_index = string.index(">")
    coordinates = string[start_index:end_index]

    print(f"Found {treasure} at {''.join(coordinates)}")
