import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Загрузка данных
url = "https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv"
data = pd.read_csv(url, sep=",")
data1 = pd.DataFrame(data)


# Выбор предикторов (независимых переменных) и зависимой переменной
X = data1.drop('quality', axis = 1)  # Признаки (все, кроме 'quality')
y = data1['quality']  # Зависимая переменная ('quality')

# Разделение данных на тренировочный и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели множественной линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Получение коэффициентов множественной линейной регрессии
coefficients = model.coef_
intercept = model.intercept_

# Вывод коэффициентов
print("Коэффициенты множественной линейной регрессии:")
for feature, coef in zip(X.columns, coefficients):
    print(f"{feature}: {coef}")

print(f"Интерсепт: {intercept}")

# Предсказание на тестовом наборе данных
y_pred = model.predict(X_test)

# Оценка модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Среднеквадратичная ошибка: {mse}")
print(f"Коэффициент детерминации (R^2): {r2}")

# Визуализация результатов (например, можно построить график реальных и предсказанных значений)
plt.scatter(y_test, y_pred)
plt.xlabel("Реальное значение")
plt.ylabel("Предсказанное значение")
plt.title("График реальных vs. предсказанных значений")
plt.show()
