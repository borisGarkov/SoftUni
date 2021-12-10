import re
line = input()
names = []
best_before = []
calories = []

pattern = r"(?P<separator>\||#)(?P<name>[a-zA-Z\s]+)(?P=separator)(?P<year>\d{2}/\d{2}/\d{2})(?P=separator)(" \
          r"?P<calories>\d+)(?P=separator)"

matches = re.finditer(pattern, line)
total_calories = 0
for match in matches:
    total_calories += int(match.group("calories"))
    names.append(match.group("name"))
    best_before.append(match.group("year"))
    calories.append(match.group("calories"))

print(f"You have food to last you for: {total_calories // 2000} days!")
if len(names) > 0:
    for food in range(len(names)):
        print(f"Item: {names[food]}, Best before: {best_before[food]}, Nutrition: {calories[food]}")