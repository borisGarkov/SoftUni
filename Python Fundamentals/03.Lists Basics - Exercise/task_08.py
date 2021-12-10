split_by_space = input().split("#")
water = int(input())
total_effort = 0
total_fire = 0
print("Cells:")

for element in split_by_space:
    split_by_equals_sign = element.split(" = ")
    current_effort = 0

    if split_by_equals_sign[0] == "High" and (81 <= int(split_by_equals_sign[1]) <= 125):
        if water - int(split_by_equals_sign[1]) >= 0:
            print(f" - {int(split_by_equals_sign[1])}")
            water -= int(split_by_equals_sign[1])
            current_effort = int(split_by_equals_sign[1]) * 0.25
            total_effort += current_effort
            total_fire += int(split_by_equals_sign[1])
        else:
            continue

    elif split_by_equals_sign[0] == "Medium" and (51 <= int(split_by_equals_sign[1]) <= 80):
        if water - int(split_by_equals_sign[1]) >= 0:
            print(f" - {int(split_by_equals_sign[1])}")
            water -= int(split_by_equals_sign[1])
            current_effort = int(split_by_equals_sign[1]) * 0.25
            total_effort += current_effort
            total_fire += int(split_by_equals_sign[1])
        else:
            continue

    elif split_by_equals_sign[0] == "Low" and (1 <= int(split_by_equals_sign[1]) <= 50):
        if water - int(split_by_equals_sign[1]) >= 0:
            print(f" - {int(split_by_equals_sign[1])}")
            water -= int(split_by_equals_sign[1])
            current_effort = int(split_by_equals_sign[1]) * 0.25
            total_effort += current_effort
            total_fire += int(split_by_equals_sign[1])
        else:
            continue

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")