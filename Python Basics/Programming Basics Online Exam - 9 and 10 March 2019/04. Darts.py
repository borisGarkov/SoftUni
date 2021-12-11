name = input()
points_left = 301
successful_shots = 0
unsuccessful_shots = 0
is_retired = False

while True:
    field = input()
    if field == "Retire":
        is_retired = True
        break

    score = int(input())
    if field == "Triple":
        score *= 3
    elif field == "Double":
        score *= 2

    if score > points_left:
        unsuccessful_shots += 1
        continue
    else:
        points_left -= score
        successful_shots += 1

    if points_left == 0:
        print(f"{name} won the leg with {successful_shots} shots.")
        break

if is_retired:
    print(f"{name} retired after {unsuccessful_shots} unsuccessful shots.")