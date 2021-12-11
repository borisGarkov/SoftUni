names = {el: {"Items": [], "Cost": []} for el in input().split(", ")}

while True:
    line = input()
    if line == "End":
        break
    name, item, cost = line.split("-")
    cost = int(cost)
    if name in names:
        if item not in names[name]["Items"]:
            names[name]["Items"].append(item)
            names[name]["Cost"].append(cost)

[print(f"{key} -> Items: {len(value['Items'])}, Cost: {sum(value['Cost'])}") for key, value in names.items()]
