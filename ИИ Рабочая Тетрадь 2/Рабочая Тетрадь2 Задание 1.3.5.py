#Рабочая Тетрадь2 Задание 1.3.5
#Задание: Создайте массив и отсортируйте его по убыванию.

import numpy as np

my_array = np.array([5, 2, 9, 1, 5, 6])

sorted_array = np.sort(my_array)[::-1]

print(sorted_array)
