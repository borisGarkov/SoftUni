n = int(input())
chemicals = set()

for _ in range(n):
    line = input().split()
    chemicals.update(line)

print("\n".join(chemicals))
