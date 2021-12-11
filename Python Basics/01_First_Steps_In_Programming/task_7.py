strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
berries_kg = float(input())
strawberries_kg = float(input())

berries_price = strawberries_price / 2
oranges_price = berries_price - (0.4 * berries_price)
bananas_price = berries_price - (0.8 * berries_price)

berries_sum = berries_price * berries_kg
oranges_sum = oranges_price * oranges_kg
bananas_sum = bananas_price * bananas_kg
strawberries_sum = strawberries_price * strawberries_kg

result = berries_sum + oranges_sum + bananas_sum + strawberries_sum
print(result)