def rate(plants_data, plant, rating):
    if plant in plants_data:
        plants_data[plant]["Rating"].append(rating)
    else:
        print("error")
    return plants_data


def update(plants_data, plant, new_rarity):
    if plant in plants_data:
        plants_data[plant]["Rarity"] = new_rarity
    else:
        print("error")
    return plants_data


def reset(plants_data, plant):
    if plant in plants_data:
        plants_data[plant]["Rating"] = []
    else:
        print("error")
    return plants_data


plants_n = int(input())
plants_data = {}

for _ in range(plants_n):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    plants_data[plant] = {"Rarity": rarity, "Rating": []}

while True:
    command_data = input().split(": ")
    command = command_data[0]
    if command == "Exhibition":
        break

    if command == "Rate":
        plant = command_data[1].split(" - ")[0]
        rating = command_data[1].split(" - ")[1]
        rating = int(rating)
        plants_data = rate(plants_data, plant, rating)
    elif command == "Update":
        plant = command_data[1].split(" - ")[0]
        new_rarity = command_data[1].split(" - ")[1]
        new_rarity = int(new_rarity)
        plants_data = update(plants_data, plant, new_rarity)
    elif command == "Reset":
        plant = command_data[1]
        plants_data = reset(plants_data, plant)

for key, value in plants_data.items():
    if sum(value["Rating"]) > 0 and len(value["Rating"]) > 0:
        value["Rating"] = sum(value["Rating"]) / len(value["Rating"])
    else:
        value["Rating"] = 0

sorted_plants = sorted(plants_data.items(), key=lambda x: (-x[1]["Rarity"], -x[1]["Rating"]))
print("Plants for the exhibition:")
for key, value in sorted_plants:
    print(f"- {key}; Rarity: {value['Rarity']}; Rating: {value['Rating']:.2f}")
