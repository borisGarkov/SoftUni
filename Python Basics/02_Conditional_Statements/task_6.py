budget = float(input())
number_of_people = int(input())
price_of_clothes = float(input())

film_decor = budget * 0.10
sum_of_clothes = number_of_people * price_of_clothes

if number_of_people > 150:
    sum_of_clothes = sum_of_clothes - (sum_of_clothes * 0.10)

total_sum = film_decor + sum_of_clothes

if total_sum > budget:
    print(f"Not enough money! \nWingard needs {total_sum - budget:.2f} leva more.")
else:
    print(f"Action! \nWingard starts filming with {budget - total_sum:.2f} leva left.")
