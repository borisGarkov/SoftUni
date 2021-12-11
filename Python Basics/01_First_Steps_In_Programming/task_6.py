days_count = int(input())
cook_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

cakes_price = 45
waffles_price = 5.80
pancakes_price = 3.20

sum_per_day = ((cakes_price * cakes_count) + (waffles_count * waffles_price) +
               (pancakes_price * pancakes_count)) * cook_count
total_sum = sum_per_day * days_count
profit = total_sum - (total_sum / 8)

print(profit)