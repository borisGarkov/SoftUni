import math

students_number = int(input())
tasks_number = int(input())
trainer_energy = int(input())

total_questions = 0
total_problems_solved = 0

while True:
    trainer_energy += 2 * tasks_number
    students_number -= tasks_number
    questions = students_number * 2
    total_questions += questions
    total_problems_solved += tasks_number
    trainer_energy -= 3 * questions

    if students_number < 10:
        print(f"The students are too few!\nProblems solved: {total_problems_solved}")
        break

    if trainer_energy <= 0:
        print(f"The trainer is too tired!\nQuestions asked: {total_questions}")
        break

    students_number += math.floor(students_number / 10)

