import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Создание датасета
x = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
target = [0, 0, 0, 1, 1, 1]

#обучение классификатора дерева решений
clf = DecisionTreeClassifier()
clf.fit(x, target)

# Пример предсказания класса для новых данных
new_data = np.array([[0, 0], [4, 4]])
predictions = clf.predict(new_data)
print(predictions)

