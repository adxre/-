import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Загрузка данных
url = "https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv"
wine_data = pd.read_csv(url)

# Посмотрим на первые несколько строк данных
wine_data.head()
# Разделяем данные на признаки (X) и целевую переменную (y)
X = wine_data.drop('quality', axis=1)
y = wine_data['quality']

# Разделяем данные на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создаем модель линейной регрессии
model = LinearRegression()

# Обучаем модель на обучающем наборе данных
model.fit(X_train, y_train)

# Делаем прогноз на тестовом наборе данных
y_pred = model.predict(X_test)

# Оцениваем точность модели
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Средняя квадратичная ошибка (MSE): {mse}")
print(f"Коэффициент детерминации (R^2): {r2}")
