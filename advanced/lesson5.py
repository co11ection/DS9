#============== Pandas ===============
#pandas - это библиотека для работы с табличными данными (EXEL, CSV, база данных) но мещнее

""" 
Работа с данными
загрузка данных с файлов EXEL, CSV базы данных

Очистка данных
Пропуски
ошибки
лишние строки

Анализ данных
# Получаем быструю статистику


Основные структуры:
Series - одномерный массив(столбец)
DataFrame - таблицы (строки + столбцы)
"""

# ======== Series ==========
# это структура данных состоящая из: значений и индексов

# Создание Series
import pandas as pd

age_series = pd.Series([23, 21, 20, 22, 34, 40])
print(age_series)
print(age_series[1])

age_series = pd.Series([23, 21, 20, 22, 34, 40],  index=['a', 'b', 'c', 'd', 'e', 'f'])
print(age_series)

age_series = pd.Series([23, 21, 20, 22, 34, 40])
print(age_series+1)
print(age_series*2)
print(age_series.mean())
print(age_series.sum())
print(age_series.max())
print(age_series.min())


# ========= DataFrame =======
data = {
    "name": ["Akyl", "Aktan", "Asan"],
    "age": [23, 20, 18]
}
df = pd.DataFrame(data,)
print(df)

#Доступы
# Столбец
print(df['name'])
# Строка
print(df.loc[0])
print(df.iloc[0])

# Добавление столбца
df['salary'] = [50000, 40000, 25000]
print(df)

# Фильтрация
print(df[df['age']>18])

# Основные методы
print(df.head(1))
print(df.info())

new_row = pd.DataFrame(
    [
        {
            "name": "Almaz",
            "age": 30,
            "salary": 60000 
        }
    ]
)
df = pd.concat([df, new_row], ignore_index=True)
print(df[['name', 'salary']])
print(df['name'])

#========= Практика ============
# Возвести все(каждый элемент) в квадра
series1 = pd.Series([1, 2, 3, 4])
print(series1 ** 2)

# Создать датафрейм, вывести среднюю цену
data = {
    "product": ["apple", "banana", 'watermelon'],
    "price": [45, 120, 150]
}

df = pd.DataFrame(data)
print(df)
print(df['price'].mean())


#Вывести тех студентов у которых баллы выше 80
data = {
    "name": ['Anna', "Almaz", "Katya"],
    "score": [60, 85, 80]
}

df = pd.DataFrame(data)
print(df[df['score']>80])

# Добавить столбец "Прошел"
# Если больше 79 то True в ином случае False

df['Прошел'] = df['score'] > 79
print(df)