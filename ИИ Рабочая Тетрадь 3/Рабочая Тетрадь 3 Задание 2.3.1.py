import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Загрузим датасет Iris
iris = load_iris()
X = iris.data
y = iris.target
k_values = [1, 5, 10]
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    
    # Разделим данные на обучающий и тестовый наборы (15% для теста)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=4)
    
    # Обучим модель
    knn.fit(X_train, y_train)
    
    # Предскажем значения на тестовом наборе
    y_pred = knn.predict(X_test)
    
    # Оценим качество модели
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# Построим график зависимости точности от k
plt.figure(figsize=(8, 6))
plt.plot(k_values, accuracies, marker='o', linestyle='-')
plt.title('Зависимость точности от количества соседей (k)')
plt.xlabel('k (количество соседей)')
plt.ylabel('Точность')
plt.grid(True)
plt.show()
