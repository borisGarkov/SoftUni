CHARS_TO_REPLACE = ["-", ",", ".", "!", "?"]


def replace_chars(line):
    for char in CHARS_TO_REPLACE:
        if char in line:
            line = line.replace(char, '@')
    return line


def print_result(text):
    [print(" ".join(line)) for line in text]


with open("text.txt", "r") as file:
    text = []
    line_counter = 0
    for line in file:
        if line_counter % 2 == 0:
            line_to_append = line.rstrip("\n")
            line_to_append = replace_chars(line_to_append).split()[::-1]
            text.append(line_to_append)
        line_counter += 1

    print_result(text)
