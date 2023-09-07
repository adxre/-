#Рабочая Тетрадь 1 Задание 4.3.3
#Задание: Дана некая функция. Построить график на интервале (0,10) с шагом 1 с заливкой площади и найти эту площадь под ним.
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
import math

# Создаем массив значений x от 0 до 10 с шагом 1
x = np.arange(0, 11, 1)

# Задаем функцию, для которой мы хотим вычислить площадь под графиком
def f(x):
    return abs(math.cos(x)*np.e**(math.cos(x)+math.log(x+1))) # Пример функции, замените ее на нужную вам функцию

# Вычисляем значения функции на заданных точках
y1 = np.vectorize(f)
y = y1(x)

# Строим график
plt.plot(x, y, 'b-')  # Строим график функции
plt.fill_between(x, y, color='lightblue')  # Заливаем площадь под графиком

# Вычисляем площадь под графиком с использованием правила трапеции
area_trapz = np.trapz(y, x)
print(f'Площадь под графиком с использованием trapz(): {area_trapz}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('График с заливкой площади')
plt.grid(True)
plt.show()
