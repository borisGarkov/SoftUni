import re

text = input()
pattern = r"(?<=(?P<char>[=|/]))[A-Z][A-Za-z]{2,}(?=(?P=char))"
valid_destinations = re.finditer(pattern, text)
destinations = []
travel_points = 0
for d in valid_destinations:
    travel_points += len(d.group())
    destinations.append(d.group())

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")