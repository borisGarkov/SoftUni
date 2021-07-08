row, col = [int(el) for el in input().split()]
matrix = [[chr(97 + r) + chr(97 + c + r) + chr(97 + r) for c in range(col)] for r in range(row)]
print('\n'.join([' '.join([matrix[r][c] for c in range(col)]) for r in range(row)]))

