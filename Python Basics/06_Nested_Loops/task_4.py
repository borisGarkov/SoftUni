members_of_jury = int(input())
grade_sum = 0
presentation_name = input()
all_grades = 0
count = 0

while presentation_name != "Finish":

    for j in range(1, members_of_jury + 1):
        presentation_grade = float(input())
        grade_sum += presentation_grade

    print(f"{presentation_name} - {(grade_sum / members_of_jury):.2f}.")
    all_grades += (grade_sum / members_of_jury)
    grade_sum = 0
    count += 1
    presentation_name = input()

print(f"Student's final assessment is {all_grades / count:.2f}.")