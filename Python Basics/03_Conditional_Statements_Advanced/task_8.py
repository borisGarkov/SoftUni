month = input()
days_spent = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = days_spent * 50
    apartment_price = days_spent * 65
    if 7 < days_spent <= 14:
        studio_price = studio_price * 0.95
    elif days_spent > 14:
        studio_price = studio_price * 0.70

elif month == "June" or month == "September":
    studio_price = days_spent * 75.20
    apartment_price = days_spent * 68.7
    if days_spent > 14:
        studio_price = studio_price * 0.80

elif month == "July" or month == "August":
    studio_price = 76 * days_spent
    apartment_price = 77 * days_spent

if days_spent > 14:
    apartment_price = apartment_price * 0.90

print(f"Apartment: {apartment_price:.2f} lv.\nStudio: {studio_price:.2f} lv.")
