def cast_spell(mana_points_data, hero_name, mp_needed, spell_name):
    if mp_needed <= mana_points_data[hero_name]:
        mana_points_data[hero_name] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {mana_points_data[hero_name]} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    return mana_points_data


def take_damage(hit_points_data, mana_points_data, hero_name, damage, attacker):
    if hit_points_data[hero_name] - damage > 0:
        hit_points_data[hero_name] -= damage
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hit_points_data[hero_name]} HP left!")
        return hit_points_data, mana_points_data
    hit_points_data.pop(hero_name)
    mana_points_data.pop(hero_name)
    print(f"{hero_name} has been killed by {attacker}!")
    return hit_points_data, mana_points_data


def recharge(mana_points_data, hero_name, amount):
    if mana_points_data[hero_name] + amount > 200:
        print(f"{hero_name} recharged for {200 - mana_points_data[hero_name]} MP!")
        mana_points_data[hero_name] = 200
        return mana_points_data
    mana_points_data[hero_name] += amount
    print(f"{hero_name} recharged for {amount} MP!")
    return mana_points_data


def heal(hit_points_data, hero_name, amount):
    if hit_points_data[hero_name] + amount > 100:
        print(f"{hero_name} healed for {100 - hit_points_data[hero_name]} HP!")
        hit_points_data[hero_name] = 100
        return hit_points_data
    hit_points_data[hero_name] += amount
    print(f"{hero_name} healed for {amount} HP!")
    return hit_points_data


heroes_number = int(input())
hit_points_data = {}
mana_points_data = {}

for _ in range(heroes_number):
    hero, hit, mana = input().split()
    hit = int(hit)
    mana = int(mana)
    hit_points_data[hero] = hit
    mana_points_data[hero] = mana

while True:
    command = input()
    if command == "End":
        break

    if command.split(" - ")[0] == "CastSpell":
        _, hero_name, mp_needed, spell_name = command.split(" - ")
        mp_needed = int(mp_needed)
        mana_points_data = cast_spell(mana_points_data, hero_name, mp_needed, spell_name)
    elif command.split(" - ")[0] == "TakeDamage":
        _, hero_name, damage, attacker = command.split(" - ")
        damage = int(damage)
        hit_points_data, mana_points_data = take_damage(hit_points_data, mana_points_data, hero_name, damage, attacker)
    elif command.split(" - ")[0] == "Recharge":
        _, hero_name, amount = command.split(" - ")
        amount = int(amount)
        mana_points_data = recharge(mana_points_data, hero_name, amount)
    elif command.split(" - ")[0] == "Heal":
        _, hero_name, amount = command.split(" - ")
        amount = int(amount)
        hit_points_data = heal(hit_points_data, hero_name, amount)

sorted_data = dict(sorted(hit_points_data.items(), key=lambda x: (-x[1], x[0])))
for key, value in sorted_data.items():
    print(key)
    print(f"  HP: {value}")
    print(f"  MP: {mana_points_data[key]}")
