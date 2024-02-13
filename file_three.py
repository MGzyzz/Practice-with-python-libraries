import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 23, 29, 28],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago'],
    'Math': [90, 85, 88, 92],
    'Physics': [80, 92, 78, 89],
    'Chemistry': [85, 90, 84, 88]
}


df = pd.DataFrame(data)

print(df)


names = df['Name']
print("\nNames:")
print(names)


older_than_25 = df[df['Age'] > 25]
print("\nOlder than 25:")
print(older_than_25)

mean_age_by_city = df.groupby('City')['Age'].mean()
print("\nMean age by city:")
print(mean_age_by_city)

df['Average'] = df[['Math', 'Physics', 'Chemistry']].mean(axis=1)

print("\nDataFrame with average grade column:")
print(df)
# Библиотека pandas это мощная и гибкая библиотека Python, предназначенная для обработки и анализа данных.
# Она предоставляет структуры данных, такие как DataFrame и Series,
# которые позволяют легко манипулировать данными, фильтровать, агрегировать и визуализировать их.
# Обьяснение кода сверху
# [1] Создать DataFrame из словаря
# [2] Выбрать столбец 'Name'
# [3] Выбрать строку с возрастом больше 25
# [4] Сгруппировать данные по городам и посчитать средний возраст
# [5] Вычисление средней оценки для каждого студента