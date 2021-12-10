population_data = {}
gold_data = {}


def case_plunder(population_data, gold_data, town, people, gold):
    if town in population_data and town in gold_data:
        population_data[town] -= people
        gold_data[town] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if population_data[town] <= 0 or gold_data[town] <= 0:
            population_data.pop(town)
            gold_data.pop(town)
            print(f"{town} has been wiped off the map!")
    return population_data, gold_data


def case_prosper(gold_dict, gold_amount, town_to_check):
    if gold_amount >= 0:
        if town_to_check in gold_dict:
            gold_dict[town_to_check] += gold_amount
            print(f"{gold_amount} gold added to the city treasury. {town} now has {gold_dict[town_to_check]} gold.")
    else:
        print("Gold added cannot be a negative number!")
    return gold_dict


while True:
    data = input()
    if data == "Sail":
        break

    town, people, gold = data.split("||")
    people = int(people)
    gold = int(gold)
    if town not in population_data:
        population_data[town] = people
        gold_data[town] = gold
    else:
        population_data[town] += people
        gold_data[town] += gold

while True:
    command = input()
    if command == "End":
        break
    if command.split("=>")[0] == "Plunder":
        _, town, people, gold = command.split("=>")
        gold = int(gold)
        people = int(people)
        population_data, gold_data = case_plunder(population_data, gold_data, town, people, gold)
    else:
        _, town, gold = command.split("=>")
        gold = int(gold)
        gold_data = case_prosper(gold_data, gold, town)

if len(population_data) > 0:
    result = dict(sorted(gold_data.items(), key=lambda x: (-x[1], x[0])))
    print(f"Ahoy, Captain! There are {len(population_data)} wealthy settlements to go to:")
    for town, value in result.items():
        print(f"{town} -> Population: {population_data[town]} citizens, Gold: {value} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
