input_line = input()
list_input = input_line.split(" ")
split_numbers = []
check_for_double_a = []
check_for_double_b = []
players_a = 11
players_b = 11

for index in list_input:
    split_numbers = index.split("-")

    if split_numbers[0] == "A":
        if split_numbers[1] not in check_for_double_a:
            check_for_double_a.append(split_numbers[1])
            players_a -= 1
        if players_a < 7:
            break
    else:
        if split_numbers[1] not in check_for_double_b:
            check_for_double_b.append(split_numbers[1])
            players_b -= 1
        if players_b < 7:
            break

print(f"Team A - {players_a}; Team B - {players_b}")

if players_a < 7 or players_b < 7:
    print("Game was terminated")

