bees_count = int(input())
health = int(input())
attack = int(input())

while True:
    bees_count -= attack
    health -= (bees_count * 5)

    if health <= 0:
        print(f"Beehive won! Bees left {bees_count}.")
        break
    if bees_count < 100:
        if bees_count < 0:
            print("The bear stole the honey! Bees left 0.")
        else:
            print(f"The bear stole the honey! Bees left {bees_count}.")
        break
