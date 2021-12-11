height_wanted = int(input())
goal_achieved = False
current_height = height_wanted - 30
unsuccessful_trials = 0
total_jumps = 0

while True:
    jump = int(input())
    total_jumps += 1

    if jump > current_height:
        if current_height >= height_wanted:
            goal_achieved = True
            break
        current_height += 5
        unsuccessful_trials = 0
    else:
        unsuccessful_trials += 1
        if unsuccessful_trials == 3:
            break

if goal_achieved:
    print(f"Tihomir succeeded, he jumped over {current_height}cm after {total_jumps} jumps.")
else:
    print(f"Tihomir failed at {current_height}cm after {total_jumps} jumps.")
