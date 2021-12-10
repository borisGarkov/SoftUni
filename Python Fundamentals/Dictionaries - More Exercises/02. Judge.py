def check_dict(dict_needed, username, contest, points, sub_dict_1, sub_dict_2):
    if username in dict_needed[contest][sub_dict_1]:
        get_index = dict_needed[contest][sub_dict_1].index(username)
        get_value = dict_needed[contest][sub_dict_2][get_index]
        if points > get_value:
            dict_needed[contest][sub_dict_2][get_index] = points
    else:
        dict_needed[contest][sub_dict_1].append(username)
        dict_needed[contest][sub_dict_2].append(points)
    return dict_needed


def check_if_name_in_dict(dict_needed, username, sub_dict_1, sub_dict_2):
    dict_needed[username] = {
        sub_dict_1: [username],
        sub_dict_2: [points]
    }
    return dict_needed


data_storage = {}
names = {}

while True:
    input_data = input().split(" -> ")
    username = input_data[0]
    if username == "no more time":
        break

    contest, points = input_data[1:]
    points = int(points)

    if username not in names:
        names = check_if_name_in_dict(names, username, "Contest", "Points")
    if contest not in data_storage:
        data_storage = check_if_name_in_dict(data_storage, contest, "Username", "Points")
    else:
        data_storage = check_dict(data_storage, username, contest, points, "Username", "Points")
        names = check_dict(names, contest, username, points, "Contest", "Points")

for key, value in data_storage.items():
    print(f"{key}: {len(value['Username'])} participants")
    temp = {}
    for check in range(len(value["Username"])):
        temp[value["Username"][check]] = value["Points"][check]
    temp = sorted(temp.items(), key=lambda x: (-x[1], x[0]))
    position = 1
    for username, points in temp:
        print(f"{position}. {username} <::> {points}")
        position += 1
