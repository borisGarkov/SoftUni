event_input_list = input().split("|")
activity_list = []
energy = 100
coins = 100
is_day_successful = True

for element in event_input_list:
    activity_list = element.split("-")
    activity = activity_list[0]
    number = int(activity_list[1])

    if activity == "rest":
        gained_energy = 0
        if energy + number > 100:
            gained_energy = 100 - energy
            energy = 100
        else:
            gained_energy = number
            energy += number

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif activity == "order":
        if energy < 30:
            energy += 50
            print("You had to rest!")
        else:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
    else:
        if coins - number > 0:
            coins -= number
            print(f"You bought {activity}.")
        else:
            is_day_successful = False
            print(f"Closed! Cannot afford {activity}.")
            break

if is_day_successful:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
