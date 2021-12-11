import math

students_number = int(input())
tasks_number = int(input())

total = students_number * math.ceil(tasks_number * 2.8)
additional_submissions = students_number * (tasks_number // 3)

total += additional_submissions
kb_needed = 5 * math.ceil(total / 10)

print(f"{kb_needed} KB needed")
print(f"{total} submissions")
