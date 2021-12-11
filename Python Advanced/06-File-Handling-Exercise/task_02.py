import re

with open("text.txt", "r") as file:
    output_text = []
    line_counter = 1
    for line in file:
        line = line.rstrip("\n")
        letters_count = len(re.findall(r"[a-zA-Z]", line))
        punct_count = len(re.findall(r"[\.\!\?\'\-\,]", line))
        output_text.append(f"Line {line_counter} {line} ({letters_count})({punct_count})\n")
        line_counter += 1

with open("output.txt", 'w') as file:
    for line in output_text:
        file.write(line)