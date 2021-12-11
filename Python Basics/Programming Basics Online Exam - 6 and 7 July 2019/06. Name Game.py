max_points = 0
winner_name = ""

while True:
    name = input()
    points = 0

    if name == "Stop":
        break

    for letter in name:
        number_input = int(input())

        if number_input == ord(letter):
            points += 10
        else:
            points += 2

    if points >= max_points:
        max_points = points
        winner_name = name

print(f"The winner is {winner_name} with {max_points} points!")

