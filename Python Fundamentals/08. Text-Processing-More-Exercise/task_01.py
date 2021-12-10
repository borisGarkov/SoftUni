n_lines = int(input())

for _ in range(n_lines):
    sentence = input()
    index = 0
    name = ""
    age = ""

    while index < len(sentence):
        char = sentence[index]
        if char == "@":
            while not char == "|":
                index += 1
                char = sentence[index]
                name += char
        elif char == "#":
            while not char == "*":
                index += 1
                char = sentence[index]
                age += char
        else:
            index += 1

    print(f"{name[:-1]} is {age[:-1]} years old.")
