#Рабочая Тетрадь 3 Задание 1.3.1
#Задание: Задайте 4 точки в трехмерном пространстве, рассчитайте между ними расстояния по описанным в примере выше метрикам. Отобразите точки
#в трехмерном пространстве.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Задаем 4 точки в трехмерном пространстве
point_a = np.array([1, 2, 3])
point_b = np.array([4, 5, 6])
point_c = np.array([2, 2, 2])
point_d = np.array([3, 3, 3])

# Вычисляем Евклидово расстояние между точками
def euclidean_distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

distance_ab = euclidean_distance(point_a, point_b)
distance_ac = euclidean_distance(point_a, point_c)
distance_ad = euclidean_distance(point_a, point_d)

# Вычисляем манхэттенское расстояние между точками
def manhattan_distance(a, b):
    return np.sum(np.abs(a - b))

manhattan_ab = manhattan_distance(point_a, point_b)
manhattan_ac = manhattan_distance(point_a, point_c)
manhattan_ad = manhattan_distance(point_a, point_d)

chebyshev_ab = np.max(np.abs(point_a - point_b))
chebyshev_ac = np.max(np.abs(point_a - point_c))
chebyshev_ad = np.max(np.abs(point_a - point_d))

# Рассчитываем расстояние Хэмминга
hamming_ab = np.sum(point_a != point_b)
hamming_ac = np.sum(point_a != point_c)
hamming_ad = np.sum(point_a != point_d)

# Отображаем точки в трехмерном пространстве
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*point_a, c='r', marker='o', label='Point A')
ax.scatter(*point_b, c='g', marker='^', label='Point B')
ax.scatter(*point_c, c='b', marker='s', label='Point C')
ax.scatter(*point_d, c='y', marker='d', label='Point D')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()

# Выводим расстояния
print("Евклидово расстояние между точкой A и B:", distance_ab)
print("Евклидово расстояние между точкой A и C:", distance_ac)
print("Евклидово расстояние между точкой A и D:", distance_ad)

print("Манхэттенское расстояние между точкой A и B:", manhattan_ab)
print("Манхэттенское расстояние между точкой A и C:", manhattan_ac)
print("Манхэттенское расстояние между точкой A и D:", manhattan_ad)

print("Расстояние Чебышева между точкой A и B:", chebyshev_ab)
print("Расстояние Чебышева между точкой A и C:", chebyshev_ac)
print("Расстояние Чебышева между точкой A и D:", chebyshev_ad)

print("Расстояние Хэмминга между точкой A и B:", hamming_ab)
print("Расстояние Хэмминга между точкой A и C:", hamming_ac)
print("Расстояние Хэмминга между точкой A и D:", hamming_ad)