#Рабочая Тетрадь 2 Задание 2.3.1
#Найдти евклидово расстояние между двумя Series (точками) a и b, не используя встроенную формулу.

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])


y = (a - b) ** 2

sum_y = np.sum(y)

euclidean_distance = np.sqrt(sum_y)

print("Евклидово расстояние между a и b:", euclidean_distance)
