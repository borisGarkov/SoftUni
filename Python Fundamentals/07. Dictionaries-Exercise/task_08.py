registry = {}

while True:
    data = input()
    if data == "End":
        break

    name, id = data.split(" -> ")

    if name not in registry:
        registry[name] = [id]
    else:
        if id not in registry[name]:
            registry[name].append(id)

registry = dict(sorted(registry.items(), key=lambda x: x[0]))
for name, id_list in registry.items():
    print(name)
    for id in id_list:
        print(f"-- {id}")