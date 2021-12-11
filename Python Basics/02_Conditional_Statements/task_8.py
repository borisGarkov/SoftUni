import math

income = float(input())
grades = float(input())
minimum_salary = float(input())

social_scholarship = math.floor(minimum_salary * 0.35)
full_scholarship = math.floor(grades * 25)

if income < minimum_salary and grades > 4.50:
    if grades >= 5.50:
        if full_scholarship >= social_scholarship:
            print(f"You get a scholarship for excellent results {full_scholarship} BGN")
        else:
            print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You get a Social scholarship {social_scholarship} BGN")

elif income >= minimum_salary and grades >= 5.50:
    print(f"You get a scholarship for excellent results {full_scholarship} BGN")

else:
    print("You cannot get a scholarship!")
