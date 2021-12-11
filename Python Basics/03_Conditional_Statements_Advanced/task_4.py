flowers_type = input()
flowers_number = int(input())
budget = int(input())

final_price = 0

if flowers_type == "Roses":
    if flowers_number > 80:
        final_price = (flowers_number * 5) * 0.9
    else:
        final_price = flowers_number * 5
elif flowers_type == "Dahlias":
    if flowers_number > 90:
        final_price = (flowers_number * 3.8) * 0.85
    else:
        final_price = flowers_number * 3.8
elif flowers_type == "Tulips":
    if flowers_number > 80:
        final_price = (flowers_number * 2.8) * 0.85
    else:
        final_price = flowers_number * 2.8
elif flowers_type == "Narcissus":
    if flowers_number < 120:
        final_price = (flowers_number * 3) * 1.15
    else:
        final_price = flowers_number * 3
elif flowers_type == "Gladiolus":
    if flowers_number < 80:
        final_price = (flowers_number * 2.5) * 1.20
    else:
        final_price = flowers_number * 2.5

if budget >= final_price:
    print(f"Hey, you have a great garden with {flowers_number} {flowers_type} and {budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(budget - final_price):.2f} leva more.")

