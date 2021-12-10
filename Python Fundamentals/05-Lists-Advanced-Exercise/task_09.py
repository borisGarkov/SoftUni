neighbourhood = [int(number) for number in input().split("@")]
total_house_number = len(neighbourhood)
house_index = 0
while True:
    command = input()
    if command == "Love!":
        break

    command = command.split()
    house_index += int(command[1])

    if house_index > len(neighbourhood) - 1:
        house_index = 0

    if neighbourhood[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
    else:
        neighbourhood[house_index] -= 2
        if neighbourhood[house_index] == 0:
            total_house_number -= 1
            print(f"Place {house_index} has Valentine's day.")


print(f"Cupid's last position was {house_index}.")
if total_house_number == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {total_house_number} places.")