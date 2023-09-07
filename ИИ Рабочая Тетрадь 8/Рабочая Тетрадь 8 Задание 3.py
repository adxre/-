import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage

# Загрузим данные об ирисах Фишера
iris = load_iris()
X = iris.data  # Все признаки
feature_names = iris.feature_names

# Выберем два признака: "длина чашелистника" и "ширина лепестка"
selected_features = [0, 3]  # Индексы признаков в массиве данных
X_selected = X[:, selected_features]
selected_feature_names = [feature_names[i] for i in selected_features]

# Стандартизируем данные (масштабирование)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_selected)

# Выполним иерархическую кластеризацию
clustering = AgglomerativeClustering(n_clusters=3)  # Количество кластеров
clustering.fit(X_scaled)

# Визуализируем результаты кластеризации
plt.figure(figsize=(10, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clustering.labels_, cmap='viridis')
plt.xlabel(selected_feature_names[0])
plt.ylabel(selected_feature_names[1])
plt.title("Hierarchical Clustering of Iris Data")
plt.show()

# Визуализируем дендрограмму
Z = linkage(X_scaled, method='ward')  # Метод "ward" для более информативной дендрограммы
plt.figure(figsize=(12, 6))
plt.title("Hierarchical Clustering Dendrogram")
dendrogram(Z, labels=clustering.labels_)
plt.show()
