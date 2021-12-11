import math

hour_input = input()
minutes_input = input()

minutes = int(minutes_input) + 15
hours = int(hour_input) * 60

hour_plus_minutes = hours + minutes

hour_output = math.floor(hour_plus_minutes / 60)
minutes_output = hour_plus_minutes % 60

if hour_output > 23:
    hour_output = 0

if minutes_output < 10:
    print(f'{hour_output}:0{minutes_output}')
else:
    print(f'{hour_output}:{minutes_output}')