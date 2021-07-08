n = [int(i) for i in input().split()]
stack = []
for i in range(0, len(n)):
    stack.append(n.pop())

print(" ".join([str(i) for i in stack]))