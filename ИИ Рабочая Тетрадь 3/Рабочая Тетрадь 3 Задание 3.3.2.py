from sklearn.feature_extraction import DictVectorizer
import pandas as pd

# Создаем пример набора данных с цветом глаз человека
data = [{'Name': 'Person1', 'EyeColor': 'Blue'},
        {'Name': 'Person2', 'EyeColor': 'Brown'},
        {'Name': 'Person3', 'EyeColor': 'Green'}]

# Инициализируем DictVectorizer
vectorizer = DictVectorizer(sparse=False)

# Преобразуем данные в матрицу признаков
X = vectorizer.fit_transform(data)

# Получаем список имен признаков
feature_names = vectorizer.get_feature_names_out()

# Создаем DataFrame из матрицы признаков
df_encoded = pd.DataFrame(X, columns=feature_names)

# Выводим матрицу признаков
print(df_encoded)
