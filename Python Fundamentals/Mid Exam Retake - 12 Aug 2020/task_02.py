people_waiting = int(input())
total_people = people_waiting
lift = [int(number) for number in input().split()]
index = 0

for index in range(len(lift)):
    while lift[index] < 4:
        lift[index] += 1
        people_waiting -= 1
        if people_waiting == 0:
            break
    if people_waiting == 0:
        break

total_number = len(lift) * 4

if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*lift)
elif people_waiting == 0 and total_number > sum(lift):
    print("The lift has empty spots!")
    print(*lift)
else:
    print(*lift)
