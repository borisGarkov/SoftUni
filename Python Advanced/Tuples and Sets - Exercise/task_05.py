contacts = {}

while True:
    line = input()
    if line.isdigit():
        break

    name, number = line.split("-")
    if name not in contacts:
        contacts[name] = 0
    contacts[name] = number

line = int(line)
for _ in range(line):
    name = input()
    if name in contacts:
        print(f"{name} -> {contacts[name]}")
    else:
        print(f"Contact {name} does not exist.")
