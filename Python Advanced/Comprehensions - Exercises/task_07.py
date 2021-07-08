line = [el for el in input().split("|")][::-1]
line = [el.split() for el in line]
matrix = []
for r in range(len(line)):
    for c in range(len(line[r])):
        matrix.append(line[r][c])

print(" ".join(matrix))

