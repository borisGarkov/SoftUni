categories = {key: [] for key in input().split(", ")}
quantities = []
qualities = []
n = int(input())

for _ in range(n):
    category, product, data = input().split(" - ")
    quantity, quality = data.split(";")
    _, n_quantity = quantity.split(":")
    _, n_quality = quality.split(":")
    n_quantity = int(n_quantity)
    n_quality = int(n_quality)

    if category in categories:
        categories[category].append(product)
        quantities.append(n_quantity)
        qualities.append(n_quality)

print(f"Count of items: {sum(quantities)}")
print(f"Average quality: {sum(qualities) / len(categories):.2f}")
[print(f"{key} -> {', '.join(value)}") for key, value in categories.items()]
