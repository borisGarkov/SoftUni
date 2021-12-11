import math

while True:
    student_name = input()
    total_points = 0
    flag = False

    if student_name == "Midnight":
        break

    for _ in range(6):
        points = int(input())

        if points < 0:
            flag = True
            break
        else:
            total_points += points

    if flag:
        print(f"{student_name} was cheating!")
        continue

    total_points = math.floor((total_points / 600) * 100)
    final_grade = total_points * 0.06

    if final_grade < 3:
        final_grade = 2

    if final_grade >= 5:
        print("===================")
        print("|   CERTIFICATE   |")
        print(f"|    {final_grade:.2f}/6.00    |")
        print("===================")
        print(f"Issued to {student_name}")
    else:
        print(f"{student_name} - {final_grade:.2f}")

