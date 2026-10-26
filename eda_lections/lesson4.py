# ================= Многомерный анализ ==================
# это иследование взаимосвязей между 3 или более пременными одновременно
# Мы должны найти скрытые структуры, убрать лишнее, понять главное


""" 
Снижение размерности - из 100 признаков оставляем 10, но без потери главной информации
Отбор признаков - какие переменные для нас важны, а что является обычным шумом
Обноружение мультиколлинерности - это когда признаки дублируются
Класстеризация - группировка обьектов по множеству признаков сразу
Визуализация высокоразмерных данных - как показать 10 измерений на 2Д экране
"""

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats
from sklearn.datasets import fetch_california_housing, load_wine

iris = sns.load_dataset('iris')

# print(sns.get_dataset_names())

penguins = sns.load_dataset("penguins").dropna()

diamonds = sns.load_dataset('diamonds')


housing = fetch_california_housing(as_frame=True).frame 

wine = load_wine(as_frame=True).frame 


# Матрица корреляции - взгляд на все связи сразу
corr_matrix = wine.drop('target', axis=1).corr()
print(corr_matrix)

# plt.figure(figsize=(12,10))
# sns.heatmap(
#     corr_matrix,
#     annot=True,
#     fmt='.2f',
#     vmin=-1,
#     vmax=1,
#     center=0,
#     cmap='RdBu_r', square=True, linewidths=0.5
# )
# plt.title("Матрица корреляции")
# plt.tight_layout()
# plt.show()


# Показать коловину матрица
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
plt.figure(figsize=(12,10))
sns.heatmap(
    corr_matrix, mask=mask, annot=True,
    fmt='.2f', center=0, square=True, cmap='RdBu_r'
)
plt.title("Толька нижняя часть")
plt.tight_layout()
plt.show()