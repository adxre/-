#Рабочая Тетрадь 2 Задание 1.3.2
#Задание: Создать 5x5 матрицу со значениями в строках от 0 до 4. Для создания необходимо использовать функцию arrange.

import numpy as np

matrix = np.arange(5).reshape(1, 5) + np.arange(5).reshape(5, 1)

print(matrix)
