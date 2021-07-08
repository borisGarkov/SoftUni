size = int(input())
matrix = [[int(x) for x in input().split(", ")] for el in range(size)]
first_diagonal = [matrix[el][el] for el in range(len(matrix))]
second_diagonal = [matrix[el][size - el - 1] for el in range(len(matrix))]

print(f"First diagonal: {', '.join([str(el) for el in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join([str(el) for el in second_diagonal])}. Sum: {sum(second_diagonal)}")
