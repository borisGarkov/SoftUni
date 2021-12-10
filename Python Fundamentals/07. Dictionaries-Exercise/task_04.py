quantities = {}
prices = {}

while True:
    data = input()
    if data == "buy":
        break
    name, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)

    if name not in quantities:
        quantities[name] = quantity
    else:
        quantities[name] += quantity

    prices[name] = price

for name, quantity in quantities.items():
    print(f"{name} -> {quantity * prices[name]:.2f}")

