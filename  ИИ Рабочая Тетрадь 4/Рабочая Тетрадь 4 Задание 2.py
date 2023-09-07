import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Загрузка данных из CSV-файла
url = "https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linear-regression/master/Salary_Data.csv"
data = pd.read_csv(url)

# Разделение данных на признаки (опыт работы) и целевую переменную (заработная плата)
X = data['YearsExperience'].values.reshape(-1, 1)
y = data['Salary'].values

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Создание и обучение модели линейной регрессии
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Получение коэффициентов линии регрессии
slope = regressor.coef_[0]
intercept = regressor.intercept_

# Вывод коэффициентов
print("Коэффициент наклона (slope):", slope)
print("Пересечение (intercept):", intercept)

# Построение прогноза
y_pred = regressor.predict(X_test)

# Визуализация данных и линии регрессии
plt.scatter(X_test, y_test, color='blue', label='Фактические данные')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Линия регрессии')
plt.title('Заработная плата от опыта работы')
plt.xlabel('Опыт работы (годы)')
plt.ylabel('Заработная плата ($)')
plt.legend()
plt.show()
