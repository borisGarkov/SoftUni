number = int(input())

bonus_points = 0
additional_bonus_points = 0

if number <= 100:
    bonus_points = 5
elif 100 < number <= 1000:
    bonus_points = number * 0.2
elif number > 1000:
    bonus_points = number * 0.1

if number % 2 == 0:
    additional_bonus_points = 1

if number % 10 == 5:
    additional_bonus_points = additional_bonus_points + 2

print(f"{additional_bonus_points + bonus_points}\n{additional_bonus_points + number + bonus_points}")