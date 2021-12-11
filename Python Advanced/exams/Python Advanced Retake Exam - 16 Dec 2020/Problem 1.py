from collections import deque

males = deque([int(el) for el in input().split()])
females = deque(map(int, input().split()))
matches = 0

while males or females:
    if len(males) == 0 or len(females) == 0:
        break
    man = males[-1]
    woman = females[0]

    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.popleft()
        continue

    if males[-1] % 25 == 0 and not males[-1] == 0:
        males.pop()
        males.pop()
        continue
    if females[0] % 25 == 0 and not females[0] == 0:
        females.popleft()
        females.popleft()
        continue

    if man == woman:
        males.pop()
        matches += 1
        females.popleft()
        continue
    else:
        males[-1] -= 2
        females.popleft()
        continue

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(el) for el in males][::-1])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print("Females left: none")
