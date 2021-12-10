snowballs_number = int(input())
snowball_value = 0
highest_snowball = 0
highest_snowball_snow = 0
highest_snowball_time = 0
highest_snowball_quality = 0

for _ in range(snowballs_number):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = pow((snowball_snow // snowball_time), snowball_quality)
    if snowball_value > highest_snowball:
        highest_snowball = snowball_value
        highest_snowball_snow = snowball_snow
        highest_snowball_time = snowball_time
        highest_snowball_quality = snowball_quality

print(f"{highest_snowball_snow} : {highest_snowball_time} = {highest_snowball} ({highest_snowball_quality})")