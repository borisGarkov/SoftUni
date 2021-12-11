budget = int(input())
season = input()
fishermen_count = int(input())

ship_rent = 0

if season == "Spring":
    ship_rent = 3000
elif season == "Summer" or season == "Autumn":
    ship_rent = 4200
else:
    ship_rent = 2600

if fishermen_count <= 6:
    ship_rent = ship_rent * 0.9
elif 7 <= fishermen_count <= 11:
    ship_rent = ship_rent * 0.85
else:
    ship_rent = ship_rent * 0.75

if fishermen_count % 2 == 0 and season != "Autumn":
    ship_rent = ship_rent * 0.95

if budget >= ship_rent:
    print(f"Yes! You have {budget - ship_rent:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget - ship_rent):.2f} leva.")