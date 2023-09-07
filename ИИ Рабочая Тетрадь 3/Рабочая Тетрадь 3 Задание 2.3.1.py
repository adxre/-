from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import numpy as np
import seaborn as sns

iris = sns.load_dataset('iris')


X_train, X_test, y_train, y_test = train_test_split(
    iris.iloc[:,:-1],
    iris.iloc[:,:-1],
    test_size=0.15
)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

X_train.head()
y_train.head()
#Обучим метод трех ближайших соседей 
model = KNeighborsClassifier(n_neighbors=3) 
model.fit(X_train, y_train)
#Получим предсказания модели
y_pred = model.predict(X_test)
y_pred
plt.figure(figsize=(10,7))
sns.scatterplot(x='petal_width',y='petal_lenght',data=iris, hue='species',s=70)
plt.xlabel('Длина лепестка, см')
plt.ylabel('Ширина лепестка, см')
plt.legend(loc=2)
plt.grid()


for i in range(len(y_test)):
    if np.array(y_test)[i] != y_pred[i]:
        plt.scatter(X_test.iloc[i, 3],X_test.iloc[i, 2], color='red',s=150)

print(f'accuracy:{accuracy_score(y_test,y_pred) :.3}')