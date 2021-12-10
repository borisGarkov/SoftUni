initial_health = 100
bitcoins = 0
dungeons_rooms = input().split("|")
best_room = 0


def case_potion(points, health):
    health_amount = 0
    if health + points > 100:
        health_amount = 100 - health
        health = 100
    else:
        health += points
        health_amount = points

    print(f"You healed for {health_amount} hp.")
    print(f"Current health: {health} hp.")
    return health


def case_chest(n_bitcoins, bitcoins):
    bitcoins += n_bitcoins
    print(f"You found {n_bitcoins} bitcoins.")
    return bitcoins


def case_monster(monster, monster_attack, health, best_room):
    if health - monster_attack > 0:
        health -= monster_attack
        print(f"You slayed {monster}.")
        return health
    else:
        print(f"You died! Killed by {monster}.")
        print(f"Best room: {best_room}")
        exit(0)


for room in dungeons_rooms:
    action, points = room.split()
    points = int(points)
    best_room += 1

    if action == "potion":
        initial_health = case_potion(points, initial_health)
    elif action == "chest":
        bitcoins = case_chest(points, bitcoins)
    else:
        initial_health = case_monster(action, points, initial_health, best_room)

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {initial_health}")
