import numpy as np
import matplotlib.pyplot as plt

# Придуманные данные
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 8, 12])

# Экстраполяция полиномом первой степени (линейным полиномом)
coeffs_linear = np.polyfit(x, y, 1)
poly_linear = np.poly1d(coeffs_linear)

# Экстраполяция полиномом второй степени
coeffs_quadratic = np.polyfit(x, y, 2)
poly_quadratic = np.poly1d(coeffs_quadratic)

# Экстраполяция полиномом третьей степени
coeffs_cubic = np.polyfit(x, y, 3)
poly_cubic = np.poly1d(coeffs_cubic)

# Генерация новых значений x для экстраполяции
x_new = np.array([6, 7, 8, 9, 10])

# Вычисление соответствующих значений y для каждого полинома
y_linear = poly_linear(x_new)
y_quadratic = poly_quadratic(x_new)
y_cubic = poly_cubic(x_new)

# Визуализация результатов
plt.figure(figsize=(10, 6))
plt.scatter(x, y, label='Исходные данные', color='blue')
plt.plot(x_new, y_linear, label='Полином 1-й степени', color='green', linestyle='--')
plt.plot(x_new, y_quadratic, label='Полином 2-й степени', color='orange', linestyle='--')
plt.plot(x_new, y_cubic, label='Полином 3-й степени', color='red', linestyle='--')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Экстраполяция полиномами')
plt.grid(True)
plt.show()
