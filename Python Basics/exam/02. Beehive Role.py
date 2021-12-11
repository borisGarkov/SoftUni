intellect = int(input())
power = int(input())
gender = input()

if intellect >= 80:
    if power >= 80 and gender == "female":
        print("Queen Bee")
    else:
        print("Repairing Bee")
elif intellect >= 60:
    print("Cleaning Bee")
else:
    if power >= 80 and gender == "male":
        print("Drone Bee")
    elif power >= 60:
        print("Guard Bee")
    else:
        print("Worker Bee")