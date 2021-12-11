import numpy as np

arr = np.array([[1, 3, 4], [3, 4, 5]], dtype=int)
arr_2 = np.array([[1, 4, 4], [3, 12, 5]])

result = arr * arr_2
print(', '.join([str(el) for el in result[0, :]]))
