stack = []
n = int(input())

for _ in range(n):
    line = input()
    command = int(line.split()[0])

    if command == 1:
        stack.append(int(line.split()[1]))
    elif command == 2 and len(stack) > 0:
        stack.pop()
    elif command == 3 and len(stack) > 0:
        print(max(stack))
    elif command == 4 and len(stack) > 0:
        print(min(stack))

stack = stack[::-1]
print(", ".join([str(i) for i in stack]))
