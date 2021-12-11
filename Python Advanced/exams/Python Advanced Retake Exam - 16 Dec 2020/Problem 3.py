def get_magic_triangle(n, triangle=[], row=0, col=0):
    if n == 0:
        return

    triangle.append([1 for el in range(row + 1)])
    if 0 > col - 1:
        triangle[row][col] = triangle[row - 1][0]
    elif col - 1 >= row - 1:
        triangle[row][col] = triangle[row - 1][-1]
    else:
        triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

    return get_magic_triangle(n, triangle=triangle, row=row, col=col)


get_magic_triangle(5)
