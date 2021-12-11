task = int(input())
points = int(input())
course = input()

if course == "Basics":
    if task == 1:
        points = points * (8 / 100)
        points = points * 0.8
    elif task == 2 or task == 3:
        points = points * (9 / 100)
    elif task == 4:
        points = points * (10 / 100)
elif course == "Fundamentals":
    if task == 1 or task == 2:
        points = points * (11 / 100)
    elif task == 3:
        points = points * (12 / 100)
    elif task == 4:
        points = points * (13 / 100)
else:
    if task == 1 or task == 2:
        points = points * (14 / 100)
        points = points * 1.20
    elif task == 3:
        points = points * (15 / 100)
        points = points * 1.20
    elif task == 4:
        points = points * (16 / 100)
        points = points * 1.20

print(f"Total points: {points:.2f}")