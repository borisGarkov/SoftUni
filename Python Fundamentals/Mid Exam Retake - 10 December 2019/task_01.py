journey_cost = float(input())
n_months = int(input())
saved_money = 0

for month in range(1, n_months + 1):
    if month != 1 and month % 2 != 0:
        spent_money = 0.16 * saved_money
        saved_money -= spent_money

    if month % 4 == 0:
        bonus_money = saved_money * 0.25
        saved_money += bonus_money

    saved_money += (journey_cost * 0.25)

if saved_money >= journey_cost:
    print(f"Bravo! You can go to Disneyland and you will have {saved_money - journey_cost:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {journey_cost - saved_money:.2f}lv. more.")
