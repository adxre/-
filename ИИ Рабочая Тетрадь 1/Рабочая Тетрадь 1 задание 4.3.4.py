import pandas as pd
import matplotlib.pyplot as plt


data = {
    'Month': [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ],
    'Apple': [
        133.61, 135.38, 172.93, 124.18, 134.07, 125.35,
        137.33, 146.95, 154.95, 142.95, 149.70, 170.30
    ],
    'Microsoft': [
        223.00, 242.50, 237.47, 242.84, 254.35, 251.29,
        271.84, 286.77, 305.19, 289.98, 331.49, 339.28
    ],
    'Google': [
        88.03, 96.12, 104.33, 107.15, 120.99, 121.90,
        126.46, 136.02, 146.82, 137.07, 148.40, 146.50
    ]
}

df = pd.DataFrame(data)

# График стоимости акций Apple
plt.figure(figsize=(12, 6))
plt.plot(df['Month'], df['Apple'], marker='o', label='Apple', linestyle='-', color='blue')

# График стоимости акций Microsoft
plt.plot(df['Month'], df['Microsoft'], marker='o', label='Microsoft', linestyle='-', color='green')

# График стоимости акций Google
plt.plot(df['Month'], df['Google'], marker='o', label='Google', linestyle='-', color='red')

# Настройка графика
plt.title('Динамика стоимости акций компаний за 12 месяцев 2021 года')
plt.xlabel('Месяц')
plt.ylabel('Стоимость акций')
plt.legend()
plt.grid(True)

# Улучшение читаемости результатов
plt.xticks(rotation=45)
plt.tight_layout()

# Отображение графика
plt.show()