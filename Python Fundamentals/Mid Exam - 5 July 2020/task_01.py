employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
total_student_number = int(input())
total_question_answered = employee_1 + employee_2 + employee_3
hours_count = 0

while total_student_number > 0:
    hours_count += 1
    if hours_count % 4 == 0:
        hours_count += 1
    total_student_number -= total_question_answered

print(f"Time needed: {hours_count}h.")
