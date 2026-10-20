# ========================= EDA =========================
# Data work - обхватывание цикла взаимодействий с данными: Начиная от сбора и очистки данных до анализва  визуализации и принятия решений на их основе

# Жизненный цикл работы с данными:
# 1) сбор данных - получение данных (бд, файл, апи, парсинг)
# 2) Очистка данных - удаление дубликатов, пропусков, исправление ошибок
#3) EDA - иследование структуры, распределение и взаимодействие с данными
#4) Моделирование - построение прогнозных и классификационных моделей
#5) Интерпретация - визуализация результатов и принятие решений 

# EDA - подход к анализу, при котором мы изучаем данные без заранее сформулированных гипотез, пытясь понять структуру данных и выявить закономерность 


# EDA - Работа с данными проводятся не единожды, а по несколько раз

import pandas as pd

df = pd.read_csv("eda_lections/magazin_orders.csv")
print(df.shape)
print(df.head(10))
# Общая информация
print(df.info())
print(df.describe())
# Пропуски
print(df.isnull().sum())

missing = (df.isnull().sum()/ len(df) * 100).round(2)
print(missing[missing > 0])


dublicate_sum = df.duplicated().sum()
print(dublicate_sum)
duplicate_by_id = df["order_id"].duplicated().sum()
print(duplicate_by_id)


dup = df[df["order_id"].duplicated(keep=False)]
print(dup.sort_values("order_id"))
print(dup[['order_id', 'customer', 'city', 'rating']])

print(df['city'].value_counts())


city_norm = df['city'].str.lower().str.strip()
print(city_norm.value_counts())
print(df['city'].mode())
# df = pd.DataFrame([1, 2 ,3])
# # mean - среднее значение
# print(df.mean())
# #median - центральное значение
# print(df.median())
# # min/max
# print(df.min())
# print(df.max())
# print(df.mode())



# Пропуски и типы пропусков
# (NaN, null, None)
# 1) MCAR - missing completely at random - полностью случайные пропуски
# 2) MAR - missing at random - случайные пропуски, зависимые
# 3) MNAR - missing not at random - не случайные пропуски

# Стратегии работы с пропусками:
# 1) Удаление строк
# print(df.dropna()) - только в случае когда пропусков мало и они < 5%
# 2) Заполнение средним значением (mean) - для числовых данных
# print(df['rating'].mean())
# df['rating'] = df['rating'].fillna(df['rating'].mean()) 5-30% MCAR
# print(df)
#3) заполнение медианой  - при наличии выбросов
# df['rating'] = df['rating'].fillna(df['rating'].median()) 5%-30%
#4) Заполнение модой - для категорий
df['city'] = df['city'].fillna(df['city'].mode()[0]) # 5-30%
print(df['city'].mode())
print(df.head(10))
# 5) Удалить столбцов только в случае когда пропуски больше 50%
# print(df.drop('city', axis=1))



# Выбросы
import seaborn as sns
print(sns.get_dataset_names())

df = sns.load_dataset('titanic')
print(df.head(10))
# Методы выбросов
# IQR - межквартильный размах

# 25 50 75
# Q1 Q2 Q3
# IQR = Q3 - Q1
# Нижняя граница = Q1 - 1.5 * IQR
# Верхняя граница = Q3 + 1.5 * IQR

# print(df['fare'].describe())

q1 = df['fare'].quantile(0.25)
q3 = df['fare'].quantile(0.75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(lower, upper)

outliers = df[(df['fare']< lower) | (df['fare']> upper)]
print(outliers[['pclass', 'sex', 'age', 'fare']])


# ВЫБРОСЫ НЕ ВСЕГДА ЯВЛЯЮТСЯ ОШИБКАМИ

# Метод Z-score

# 165 166 167 168 198
# Z = 1.5


# Z = (x - mean) / std)
# std - стандартное отклонение
# x - значение
# mean - среднее значение
print(df['fare'].describe()) 
from scipy import stats

