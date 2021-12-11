import math

students_number = int(input())
seasons_number = int(input())

total_students = 0

for season in range(1, seasons_number + 1):
    first_exam = math.ceil(students_number * 0.9)
    second_exam = math.ceil(first_exam * 0.9)
    pass_students = math.ceil(second_exam * 0.8)

    if season % 3 == 0:
        retake_students = math.ceil(pass_students * 0.15)
    else:
        retake_students = math.ceil(pass_students * 0.05)

    total_students = pass_students + retake_students
    students_number = total_students

print(f"Students: {total_students}")
