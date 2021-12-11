budget = float(input())
line = input()
product_count = 0
total_price = 0

while line != "Stop":
    product_price = float(input())
    product_count += 1

    if product_count % 3 == 0:
        product_price /= 2

    if product_price > budget:
        print(f"You don't have enough money!\nYou need {product_price - budget:.2f} leva!")
        break

    total_price += product_price
    budget -= product_price
    line = input()

if line == "Stop":
    print(f"You bought {product_count} products for {total_price:.2f} leva.")