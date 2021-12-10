import re
total_price = 0
while True:
    line = input()
    if line == "end of shift":
        break

    pattern = r"%(?P<name>[A-Z][a-z]+)%[^\|\$%\.]*<(?P<product>[\w]+)>[^\|\$%\.]*\|(?P<quantity>[\d]+)\|[^\|\$%\.]*?(?P<price>[\d]+\.?[\d]+)\$"
    valid_customers = re.finditer(pattern, line)

    for customer in valid_customers:
        price = int(customer.group('quantity')) * float(customer.group('price'))
        total_price += price
        print(f"{customer.group('name')}: {customer.group('product')} - {price:.2f}")

print(f"Total income: {total_price:.2f}")

