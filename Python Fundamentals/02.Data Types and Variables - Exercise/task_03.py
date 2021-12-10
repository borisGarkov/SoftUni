people_number = int(input())
capacity = int(input())
courses_count = 0
flag = False

if capacity >= people_number:
    print(1)
else:
    flag = True
    while people_number > 0:
        people_number -= capacity
        courses_count += 1

if flag:
    print(courses_count)