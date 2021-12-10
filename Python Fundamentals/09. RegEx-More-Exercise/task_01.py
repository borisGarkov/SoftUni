import re

names_data = input().split(", ")
participants = {}

while True:
    line = input()
    if line == "end of race":
        break

    pattern = r"[A-Za-z]+"
    current_name = ""
    name_as_char = re.findall(pattern, line)
    for char in name_as_char:
        current_name += char

    pattern_digits = r"\d"
    digits_data = re.findall(pattern_digits, line)
    digits_sum = 0
    for digit in digits_data:
        digits_sum += int(digit)

    if current_name not in participants and current_name in names_data:
        participants[current_name] = digits_sum
    elif current_name in names_data:
        participants[current_name] += digits_sum

sorted_participants = dict(sorted(participants.items(), key=lambda x: x[1], reverse=True))
result = list(sorted_participants.keys())
print(f"1st place: {result[0]}")
print(f"2nd place: {result[1]}")
print(f"3rd place: {result[2]}")
