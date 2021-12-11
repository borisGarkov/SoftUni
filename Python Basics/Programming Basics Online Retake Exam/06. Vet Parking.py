days = int(input())
hours = int(input())
total_fee = 0

for day in range(1, days + 1):
    parking_fee = 0
    for hour in range(1, hours + 1):

        if day % 2 == 0 and hour % 2 != 0:
            parking_fee += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            parking_fee += 1.25
        else:
            parking_fee += 1

    total_fee += parking_fee
    print(f"Day: {day} - {parking_fee:.2f} leva")

print(f"Total: {total_fee:.2f} leva")