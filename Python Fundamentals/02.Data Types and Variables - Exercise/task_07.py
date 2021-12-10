final_number = int(input())
tank_capacity = 255
total_current_liters = 0

for iterator in range(final_number):
    water_liters = int(input())
    total_current_liters += water_liters

    if total_current_liters > tank_capacity:
        total_current_liters -= water_liters
        print("Insufficient capacity!")

print(total_current_liters)