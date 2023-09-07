import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Загрузите данные ирисов Фишера
data = load_iris()
X = data.data
# Экспериментируйте с разным количеством кластеров
cluster_counts = [2, 3, 4, 5]

for n_clusters in cluster_counts:
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(X)
    cluster_labels = kmeans.labels_

    # Визуализация кластеров (примечание: для 2D данных)
    plt.scatter(X[:, 0], X[:, 1], c=cluster_labels)
    plt.title(f'K-Means с {n_clusters} кластерами')
    plt.show()
