import re

health_data = {}
damage_data = {}

demons_data = input().replace(" ", "").split(",")
for demon in demons_data:

    demon_health = 0
    pattern_letters = r"[A-Za-z]"
    demon_letters_match = re.findall(pattern_letters, demon)
    for d in demon_letters_match:
        demon_health += ord(d)

    demon_damage = 0
    pattern_digits = r"[-+]?\d+\.?\d+|[-+]?\d+"
    demon_digits_match = re.findall(pattern_digits, demon)
    for d in demon_digits_match:
        demon_damage += float(d)

    for char in demon:
        if char == "*":
            demon_damage *= 2
        elif char == "/":
            demon_damage /= 2

    health_data[demon] = demon_health
    damage_data[demon] = demon_damage

health_data = dict(sorted(health_data.items(), key=lambda x: x[0]))
for name, value in health_data.items():
    print(f"{name} - {value} health, {damage_data[name]:.2f} damage")
