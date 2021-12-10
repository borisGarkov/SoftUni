import re
count = int(input())
pattern = r"[STARstar]"
attacked_planets = []
destroyed_planets = []

for _ in range(count):
    line = input()
    special_chars_length = len(re.findall(pattern, line))

    result = ""
    for char in line:
        char = chr(ord(char) - special_chars_length)
        result += char

    pattern_planets = r"@(?P<planet>[A-Za-z]+)[^@\-\!:>]*:(?P<population>[\d]+)![^@\-\!:>]*(?P<attack_type>A|D)![" \
                      r"^@\-\!:>]*\->(?P<soldier_count>[\d]+)"
    planets = re.finditer(pattern_planets, result)
    for planet in planets:
        if planet.group("attack_type") == "A":
            attacked_planets.append(planet.group("planet"))
        elif planet.group("attack_type") == "D":
            destroyed_planets.append(planet.group("planet"))

print(f"Attacked planets: {len(attacked_planets)}")
if len(attacked_planets) > 0:
    for planet in sorted(attacked_planets):
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
if len(destroyed_planets) > 0:
    for planet in sorted(destroyed_planets):
        print(f"-> {planet}")