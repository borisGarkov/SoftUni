import math

record_seconds = float(input())
distance_meters = float(input())
time_to_swim = float(input())

distance_to_swim = distance_meters * time_to_swim
additional_time_to_swim = math.floor(distance_meters / 15) * 12.5

total_time = distance_to_swim + additional_time_to_swim

if total_time >= record_seconds:
    print(f"No, he failed! He was {total_time - record_seconds:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

