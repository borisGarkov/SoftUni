from collections import deque

n = int(input())
queue = deque()
running_total_petrol = 0

for i in range(n):
    temp = [int(x) for x in input().split()]
    queue.append(temp)

for big_circle in range(n):
    is_valid = True
    for small_circle in range(n):
        successful_index = big_circle
        current_petrol, current_destination = queue[small_circle]
        running_total_petrol += current_petrol - current_destination
        if running_total_petrol < 0:
            running_total_petrol = 0
            queue.append(queue.popleft())
            is_valid = False
            break
    if is_valid:
        print(successful_index)
        break
