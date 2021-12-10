times_to_pass = [int(time) for time in input().split()]
middle_point = len(times_to_pass) // 2
left_side = times_to_pass[:middle_point]
right_side = times_to_pass[middle_point + 1:]

winner = ""
final_time = 0
sum_left = 0
sum_right = 0

for time in left_side:
    sum_left += time
    if time == 0:
        sum_left *= 0.8

for time in right_side:
    sum_right += time
    if time == 0:
        sum_right *= 0.8

if sum_left < sum_right:
    winner = "left"
    final_time = sum_left
else:
    winner = "right"
    final_time = sum_right

print(f"The winner is {winner} with total time: {final_time:.1f}")