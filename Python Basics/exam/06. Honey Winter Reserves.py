honey_amount = float(input())
total_production = 0

while True:
    line = input()

    if line == "Winter has come":
        break

    for month in range(6):
        production = float(input())
        total_production += production

    if total_production >= honey_amount:
        break
    elif total_production < 0:
        print(f"{line} was banished for gluttony")

honey_left = abs(total_production - honey_amount)
if total_production >= honey_amount:
    print(f"Well done! Honey surplus {honey_left:.2f}.")
else:
    print(f"Hard Winter! Honey needed {honey_left:.2f}.")