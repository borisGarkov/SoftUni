total_price = 0

while True:
    input_line = input()
    if input_line == "special" or input_line == "regular":
        break

    price = float(input_line)
    if price < 0:
        print("Invalid price!")
        continue

    total_price += price

price_before_tax = total_price
taxes = total_price * 0.2
total_price += taxes
if input_line == "special":
    total_price *= 0.9

if price_before_tax == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\n"
      f"Price without taxes: {price_before_tax:.2f}$\n"
      f"Taxes: {taxes:.2f}$\n"
      f"-----------\n"
      f"Total price: {total_price:.2f}$")
