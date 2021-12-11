initial_budget = float(input())
season = input()

final_budget = 0
destination = ""
place_to_stay = ""

if initial_budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place_to_stay = "Camp"
        final_budget = initial_budget * 0.3
    else:
        place_to_stay = "Hotel"
        final_budget = initial_budget * 0.7
elif 100 < initial_budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place_to_stay = "Camp"
        final_budget = initial_budget * 0.4
    else:
        place_to_stay = "Hotel"
        final_budget = initial_budget * 0.8
else:
    destination = "Europe"
    place_to_stay = "Hotel"
    final_budget = initial_budget * 0.9

print(f"Somewhere in {destination}\n{place_to_stay} - {final_budget:.2f}")
