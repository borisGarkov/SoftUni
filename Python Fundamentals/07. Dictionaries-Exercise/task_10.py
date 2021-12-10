courses_dict = {}
max_points = {}

while True:
    data = input()
    if data == "exam finished":
        break
    if data.split("-")[1] == "banned":
        name, _ = data.split("-")
        if name in max_points:
            max_points.pop(name)
    else:
        name, course, points = data.split("-")
        points = int(points)
        if course not in courses_dict:
            courses_dict[course] = [name]
        else:
            courses_dict[course].append(name)

        if name not in max_points:
            max_points[name] = points
        else:
            for key, value in max_points.items():
                if key == name:
                    if points > value:
                        max_points[name] = points

sorted_max_points = sorted(max_points.items(), key=lambda x: (-x[1], x[0]))
sorted_courses = sorted(courses_dict.items(), key=lambda x: (-len(x[1]), x[0]))
print("Results:")
for username, points in sorted_max_points:
    print(f"{username} | {points}")
print("Submissions:")
for language, submissions_count in sorted_courses:
    print(f"{language} - {len(submissions_count)}")


