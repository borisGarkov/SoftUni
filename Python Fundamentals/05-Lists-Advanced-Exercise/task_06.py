numbers_list = [int(number) for number in input().split(", ")]
boundary = 10

while len(numbers_list) > 0:
    boundary_list = [numbers_list[number] for number in range(len(numbers_list)) if numbers_list[number] <= boundary]
    numbers_list = [numbers_list[number] for number in range(len(numbers_list)) if numbers_list[number] > boundary]
    print(f"Group of {boundary}'s: {boundary_list}")
    boundary += 10