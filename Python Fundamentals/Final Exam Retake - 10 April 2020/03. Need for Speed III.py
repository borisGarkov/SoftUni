def drive(mileage_data, fuel_data, car, distance, fuel_needed):
    if fuel_data[car] < fuel_needed:
        print("Not enough fuel to make that ride")
    else:
        mileage_data[car] += distance
        fuel_data[car] -= fuel_needed
        print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")

    if mileage_data[car] >= 100000:
        mileage_data.pop(car)
        fuel_data.pop(car)
        print(f"Time to sell the {car}!")
    return mileage_data, fuel_data


def refuel(fuel_data, car, fuel_to_refill):
    if fuel_data[car] + fuel_to_refill > 75:
        print(f"{car} refueled with {75 - fuel_data[car]} liters")
        fuel_data[car] = 75
    else:
        print(f"{car} refueled with {fuel_to_refill} liters")
        fuel_data[car] += fuel_to_refill
    return fuel_data


def revert(mileage_data, car, kilometers):
    mileage_data[car] -= kilometers
    if mileage_data[car] >= 10000:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    else:
        mileage_data[car] = 10000
    return mileage_data


cars_number = int(input())
mileage_data = {}
fuel_data = {}

for _ in range(cars_number):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    mileage_data[car] = mileage
    fuel_data[car] = fuel

while True:
    command_data = input().split(" : ")
    command = command_data[0]
    if command == "Stop":
        break

    if command == "Drive":
        _, car, distance, fuel_needed = command_data
        distance = int(distance)
        fuel_needed = int(fuel_needed)
        mileage_data, fuel_data = drive(mileage_data, fuel_data, car, distance, fuel_needed)
    elif command == "Refuel":
        _, car, fuel_to_refill = command_data
        fuel_to_refill = int(fuel_to_refill)
        fuel_data = refuel(fuel_data, car, fuel_to_refill)
    elif command == "Revert":
        _, car, kilometers = command_data
        kilometers = int(kilometers)
        mileage_data = revert(mileage_data, car, kilometers)

sorted_car = sorted(mileage_data.items(), key=lambda x: (-x[1], x[0]))
for key, value in sorted_car:
    print(f"{key} -> Mileage: {value} kms, Fuel in the tank: {fuel_data[key]} lt.")
