fireworks = [int(el) for el in input().split(", ")]
explosives = [int(el) for el in input().split(", ")]

palm = 0
willow = 0
crossette = 0

while True:
    if len(explosives) == 0 or len(fireworks) == 0:
        break
    f = fireworks[0]
    ex = explosives[-1]

    if f <= 0 or ex <= 0:
        if f <= 0:
            fireworks = fireworks[1:]
        if ex <= 0:
            explosives = explosives[:-1]
        continue

    current_sum = f + ex

    if current_sum % 5 != 0 and current_sum % 3 == 0:
        palm += 1
        fireworks = fireworks[1:]
        explosives = explosives[:-1]
        continue

    if current_sum % 5 == 0 and current_sum % 3 != 0:
        willow += 1
        fireworks = fireworks[1:]
        explosives = explosives[:-1]
        continue

    if current_sum % 3 == 0 and current_sum % 5 == 0:
        crossette += 1
        fireworks = fireworks[1:]
        explosives = explosives[:-1]
        continue

    fireworks[0] -= 1
    fireworks = fireworks[1:] + fireworks[:1]

if palm >= 3 and willow >= 3 and crossette >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join([str(el) for el in fireworks])}")
if explosives:
    print(f"Explosive Power left: {', '.join([str(el) for el in explosives])}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")
