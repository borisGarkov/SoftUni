import re

n = int(input())
pattern = r"\|(?P<name>[A-Z]+)\|:#(?P<title>([A-Za-z]+\s[A-Za-z]+))#"
for _ in range(n):
    line = input()

    match = re.match(pattern, line)
    if match:
        name = match.group("name")
        title = match.group("title")
        print(f"{name}, The {title}")
        print(f">> Strength: {len(name)}")
        print(f">> Armour: {len(title)}")
    else:
        print("Access denied!")