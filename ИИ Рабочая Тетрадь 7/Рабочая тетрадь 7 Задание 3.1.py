import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Загрузим данные о наборе данных Iris
data = load_iris()
X = data.data
y = data.target

# Разделим данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создадим и обучим MLPClassifier
clf = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
clf.fit(X_train, y_train)

# Предсказание на тестовых данных
y_pred = clf.predict(X_test)

# Оценка точности модели
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
