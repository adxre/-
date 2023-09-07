#Рабочая Тетрадь 2 задание 1.3.4
#Задание: Создать матрицу с 0 внутри, и 1 на границах.

import numpy as np

rows, cols = 5, 5  


matrix = np.zeros((rows, cols), dtype=int)


matrix[0, :] = 1  
matrix[-1, :] = 1  
matrix[:, 0] = 1  
matrix[:, -1] = 1  

print(matrix)
