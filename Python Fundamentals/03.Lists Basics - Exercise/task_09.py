input_line_list = input().split("|")
budget = float(input())
list_new_prices = []
total_spent = 0
total_revenue = 0

for element in input_line_list:
    clothes_price_list = element.split("->")
    new_price = 0.0

    if clothes_price_list[0] == "Clothes" and float(clothes_price_list[1]) <= 50:
        if float(clothes_price_list[1]) > budget:
            continue
        else:
            budget -= float(clothes_price_list[1])
            new_price = float(clothes_price_list[1]) * 1.40
            total_spent += float(clothes_price_list[1])
            list_new_prices.append(new_price)
    elif clothes_price_list[0] == "Shoes" and float(clothes_price_list[1]) <= 35:
        if float(clothes_price_list[1]) > budget:
            continue
        else:
            budget -= float(clothes_price_list[1])
            new_price = float(clothes_price_list[1]) * 1.40
            total_spent += float(clothes_price_list[1])
            list_new_prices.append(new_price)
    elif clothes_price_list[0] == "Accessories" and float(clothes_price_list[1]) <= 20.50:
        if float(clothes_price_list[1]) > budget:
            continue
        else:
            budget -= float(clothes_price_list[1])
            new_price = float(clothes_price_list[1]) * 1.40
            total_spent += float(clothes_price_list[1])
            list_new_prices.append(new_price)

for element in list_new_prices:
    total_revenue += float(element)

final_list = []

for element in list_new_prices:
    formatted_float = "{:.2f}".format(element)
    final_list.append(formatted_float)

print(*final_list)
print(f"Profit: {total_revenue - total_spent:.2f}")
if (budget + total_revenue) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")