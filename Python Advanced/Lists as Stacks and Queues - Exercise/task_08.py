from collections import deque

green_light = int(input())
free_window = int(input())

total_cars_passed = 0
cars = deque()

while True:
    total_time = green_light + free_window

    command = input()
    if command == "END":
        break

    if not command == "green":
        cars.append(command)

    if command == "green":
        while True:
            if cars:
                current_car = list(cars.popleft())
                if len(current_car) <= total_time:
                    total_cars_passed += 1
                    total_time -= len(current_car)
                    if free_window >= total_time:
                        break
                else:
                    hit = len(current_car) - total_time
                    print("A crash happened!")
                    print(f"{''.join(current_car)} was hit at {current_car[-hit]}.")
                    exit()
            else:
                break

print("Everyone is safe.")
print(f"{total_cars_passed} total cars passed the crossroads.")