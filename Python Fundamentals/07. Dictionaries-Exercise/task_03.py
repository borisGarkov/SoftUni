legendary_items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
is_win = False

while True:
    data = input().split()
    while len(data) != 0:
        value = int(data[0])
        element = data[1].lower()

        if element == "shards" or element == "fragments" or element == "motes":
            legendary_items[element] += value

            if legendary_items.get("shards") >= 250:
                legendary_items["shards"] -= 250
                is_win = True
                print("Shadowmourne obtained!")
                break

            if legendary_items.get("fragments") >= 250:
                legendary_items["fragments"] -= 250
                is_win = True
                print("Valanyr obtained!")
                break

            if legendary_items.get("motes") >= 250:
                legendary_items["motes"] -= 250
                is_win = True
                print("Dragonwrath obtained!")
                break
        else:
            if element not in junk_items:
                junk_items[element] = value
            else:
                junk_items[element] += value

        data.pop(1)
        data.pop(0)

    if is_win:
        break

legendary_items = dict(sorted(legendary_items.items(), key=lambda item: (-item[1], item[0])))
junk_items = dict(sorted(junk_items.items(), key=lambda item: item[0]))

for key, item in legendary_items.items():
    print(f"{key}: {item}")
for key, item in junk_items.items():
    print(f"{key}: {item}")
