contests = {}
final_data = {}
while True:
    input_data = input().split(":")
    contest = input_data[0]
    if contest == "end of contests":
        break
    contests[contest] = input_data[1]

while True:
    input_data = input().split("=>")
    contest = input_data[0]
    if contest == "end of submissions":
        break

    password, username, points = input_data[1:]
    points = int(points)
    if contest in contests:
        if password == contests[contest]:
            if username not in final_data:
                final_data[username] = {"Contest": [contest], "Points": [points]}
            else:
                if contest not in final_data[username]["Contest"]:
                    final_data[username]["Contest"].append(contest)
                    final_data[username]["Points"].append(points)

                get_index = final_data[username]["Contest"].index(contest)
                get_value = final_data[username]["Points"][get_index]
                if contest in final_data[username]["Contest"] and get_value < points:
                    final_data[username]["Points"][get_index] = points

max_total_points = 0
top_user = ""
for key, value in final_data.items():
    current_points = sum(value["Points"])
    if current_points > max_total_points:
        max_total_points = current_points
        top_user = key

print(f"Best candidate is {top_user} with total {max_total_points} points.")
print("Ranking:")
sorted_data = sorted(final_data.items(), key=lambda x: x[0])
for key, value in sorted_data:
    print(key)
    temp = {}
    for check in range(len(value["Contest"])):
        temp[value["Contest"][check]] = value["Points"][check]
    temp = sorted(temp.items(), key=lambda x: -x[1])
    for contest, points in temp:
        print(f"#  {contest} -> {points}")