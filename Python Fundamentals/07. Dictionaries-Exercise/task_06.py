registrar = {}

while True:
    data = input()
    if data == "end":
        break

    course, student = data.split(" : ")
    if course not in registrar:
        registrar[course] = [student]
    else:
        registrar[course].append(student)

registrar = dict(sorted(registrar.items(), key=lambda x: len(x[1]), reverse=True))

for course, student_list in registrar.items():
    print(f"{course}: {len(student_list)}")
    student_list.sort()
    for student in student_list:
        print(f"-- {student}")