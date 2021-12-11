poor_marks = int(input())
task_name = ""
grade = 0
score = 0
problems_count = 0
last_task = ""
poor_marks_count = 0

while poor_marks_count < poor_marks:
    task_name = input()

    if task_name == "Enough":
        print(f"Average score: {score / problems_count:.2f}\nNumber of problems: {problems_count}"
              f"\nLast problem: {last_task}")
        break

    grade = int(input())
    if grade <= 4:
        poor_marks_count += 1

    if poor_marks_count == poor_marks:
        print(f"You need a break, {poor_marks_count} poor grades.")

    last_task = task_name
    score += grade
    problems_count += 1
