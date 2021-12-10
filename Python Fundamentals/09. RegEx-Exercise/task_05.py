import re
total_price = 0
furniture_list = []

while True:
    line = input()
    if line == "Purchase":
        break

    pattern = r">>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+\.?\d+)!(?P<quantity>\d+)"
    matches = re.finditer(pattern, line)
    for match in matches:
        total_price += float(match.group("price")) * float(match.group("quantity"))
        furniture_list.append(match.group("furniture"))

print("Bought furniture:")
if len(furniture_list) > 0:
    print("\n".join(furniture_list))
print(f"Total money spend: {total_price:.2f}")