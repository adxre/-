#Рабочая Тетрадь 1 Задание 3.3.5
#Задание: Задайте массив случайных значений из интервала(0; 1).
#Рассчитайте средние и медианные значения для массива, сравните
#результаты, какие выводы можно сделать о значениях?
#Постройте точечную диаграмму рассения полученного ряда.

import numpy as np
import matplotlib.pyplot as plt

# Создаем массив случайных значений из интервала (0, 1)
np.random.seed(42)  # Зафиксируем seed для воспроизводимости результатов
data = np.random.rand(100)  # Создаем массив из 100 случайных значений

# Рассчитываем среднее и медиану
mean_value = np.mean(data)
median_value = np.median(data)

# Выводим результаты
print(f"Среднее значение: {mean_value}")
print(f"Медианное значение: {median_value}")

# Строим точечную диаграмму рассеяния
plt.scatter(range(len(data)), data, alpha=0.5)
plt.xlabel('Индекс элемента')
plt.ylabel('Значение')
plt.title('Точечная диаграмма рассеяния')
plt.axhline(mean_value, color='red', linestyle='dashed', label='Среднее значение')
plt.axhline(median_value, color='green', linestyle='dashed', label='Медианное значение')
plt.legend()
plt.show()
