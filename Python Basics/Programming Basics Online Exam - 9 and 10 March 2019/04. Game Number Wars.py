first_player = input()
second_player = input()
first_points = 0
second_points = 0
winner = ""
final_points = 0

while True:
    first_line = input()
    if first_line == "End of game":
        print(f"{first_player} has {first_points} points\n{second_player} has {second_points} points")
        break

    second_line = input()
    first_card = int(first_line)
    second_card = int(second_line)
    difference = abs(first_card - second_card)

    if first_card > second_card:
        first_points += difference
    elif second_card > first_card:
        second_points += difference
    else:
        print("Number wars!")
        first_card = int(input())
        second_card = int(input())

        if first_card > second_card:
            winner = first_player
            final_points = first_points
        else:
            winner = second_player
            final_points = second_points

        print(f"{winner} is winner with {final_points} points")
        break
