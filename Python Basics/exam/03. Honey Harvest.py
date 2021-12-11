flower_type = input()
count_flowers = int(input())
season = input()

honey_harvested = 0

if season == "Spring":
    if flower_type == "Sunflower":
        honey_harvested += count_flowers * 10
    elif flower_type == "Daisy":
        honey_harvested += count_flowers * 12
        honey_harvested *= 1.10
    elif flower_type == "Lavender":
        honey_harvested += count_flowers * 12
    else:
        honey_harvested += count_flowers * 10
        honey_harvested *= 1.10
elif season == "Summer":
    if flower_type == "Sunflower":
        honey_harvested += count_flowers * 8
        honey_harvested *= 1.10
    elif flower_type == "Daisy":
        honey_harvested += count_flowers * 8
        honey_harvested *= 1.10
    elif flower_type == "Lavender":
        honey_harvested += count_flowers * 8
        honey_harvested *= 1.10
    else:
        honey_harvested += count_flowers * 12
        honey_harvested *= 1.10
else:
    if flower_type == "Sunflower":
        honey_harvested += count_flowers * 12
        honey_harvested *= 0.95
    elif flower_type == "Daisy":
        honey_harvested += count_flowers * 6
        honey_harvested *= 0.95
    elif flower_type == "Lavender":
        honey_harvested += count_flowers * 6
        honey_harvested *= 0.95
    else:
        honey_harvested += count_flowers * 6
        honey_harvested *= 0.95

print(f"Total honey harvested: {honey_harvested:.2f}")