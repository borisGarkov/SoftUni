records = {}

while True:
    command_data = input().split(":")
    command = command_data[0]
    if command == "Results":
        break

    if command == "Add":
        name, health, energy = command_data[1:]
        health = int(health)
        energy = int(energy)
        if name not in records:
            records[name] = {"health": health, "energy": energy}
        else:
            records[name]["health"] += health
    elif command == "Attack":
        attacker, defender, damage = command_data[1:]
        damage = int(damage)
        if attacker in records and defender in records:
            records[defender]["health"] -= damage
            records[attacker]["energy"] -= 1
            if records[defender]["health"] <= 0:
                records.pop(defender)
                print(f"{defender} was disqualified!")
            if records[attacker]["energy"] <= 0:
                records.pop(attacker)
                print(f"{attacker} was disqualified!")
    elif command == "Delete":
        username = command_data[1]
        if username == "All":
            records = {}
        else:
            records.pop(username)

sorted_records = sorted(records.items(), key=lambda x: (-x[1]["health"], x[0]))
print(f"People count: {len(sorted_records)}")
for key, value in sorted_records:
    print(f"{key} - {value['health']} - {value['energy']}")
