budget = float(input())
flour_price = float(input())
eggs_count = 0
cozonac_count = 0

eggs_price = flour_price * 0.75
full_milk_price = flour_price * 1.25
quarter_milk_price = full_milk_price * 0.25
cozonac_price = flour_price + eggs_price + quarter_milk_price

while True:
    if cozonac_price > budget:
        break

    budget -= cozonac_price
    eggs_count += 3
    cozonac_count += 1

    if cozonac_count % 3 == 0:
        eggs_count -= cozonac_count - 2

print(f"You made {cozonac_count} cozonacs! Now you have {eggs_count} eggs and {budget:.2f}BGN left.")