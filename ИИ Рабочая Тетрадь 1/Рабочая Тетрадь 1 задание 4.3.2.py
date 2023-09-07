#Рабочая Тетрадь 1 Задание 4.3.2
#Задание: Дана некая  функция. Создать массив из 10 значений функции (𝑥, например, изменяется от 1 до 10). Выделить срез первой
#половины массива и построить графики для основного массива – линейный и для среза – точечный
import numpy as np
import math
import matplotlib.pyplot as plt

# Создаем массив значений x от 1 до 10
x = np.linspace(1, 10, 10)

# Определяем функцию, которую нужно вычислить
def my_function(x):
    return (math.sqrt(1+ math.e**math.sqrt(x)+np.cos(x**2))/abs(1-(np.sin(x))**2)) + np.log(abs(2*x))

# Вычисляем значения функции для всего массива x
y1 = np.vectorize(my_function)
y = y1(x)

# Выделяем срез первой половины массива
half_index = len(x) // 2
x_slice = x[:half_index]
y_slice = y[:half_index]

# Строим график для основного массива (линейный)
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x, y, 'b.-')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График для основного массива')

# Строим график для среза (точечный)
plt.subplot(1, 2, 2)
plt.scatter(x_slice, y_slice, c='r', marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График для среза')

plt.tight_layout()
plt.show()
