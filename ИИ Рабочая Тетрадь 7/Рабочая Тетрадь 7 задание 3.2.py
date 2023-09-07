import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Загрузим данные о зависимости заработной платы от опыта работы
url = "https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linearregression/master/Salary_Data.csv"
data = pd.read_csv(url)

# Разделим данные на признаки (опыт работы) и целевую переменную (заработная плата)
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Разделим данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создадим и обучим MLPRegressor
regressor = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
regressor.fit(X_train, y_train)

# Предсказание на тестовых данных
y_pred = regressor.predict(X_test)

# Оценка качества модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Визуализация результата
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.xlabel('Опыт работы (годы)')
plt.ylabel('Заработная плата')
plt.title('Зависимость заработной платы от опыта работы')
plt.show()
