import math

exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

exam_total = (exam_hours * 60) + exam_minutes
arrival_total = (arrival_hours * 60) + arrival_minutes

difference = arrival_total - exam_total
difference_opposite = exam_total - arrival_total


if arrival_total > exam_total:
    difference_hours = math.floor(difference / 60)
    difference_minutes = difference % 60

    if difference < 60:
        print(f"Late\n{difference} minutes after the start")
    else:
        if difference_minutes < 10:
            print(f"Late\n{difference_hours}:0{difference_minutes} hours after the start")
        else:
            print(f"Late\n{difference_hours}:{difference_minutes} hours after the start")

elif arrival_total == exam_total or difference_opposite <= 30:
    if arrival_total == exam_total:
        print("On time")
    else:
        print(f"On time\n{difference_opposite} minutes before the start")

else:
    difference_hours_opposite = math.floor(difference_opposite / 60)
    difference_minutes_opposite = difference_opposite % 60

    if 30 < difference_opposite < 60:
        print(f"Early\n{difference_opposite} minutes before the start")
    else:
        if difference_minutes_opposite < 10:
            print(f"Early\n{difference_hours_opposite}:0{difference_minutes_opposite} hours before the start")
        else:
            print(f"Early\n{difference_hours_opposite}:{difference_minutes_opposite} hours before the start")