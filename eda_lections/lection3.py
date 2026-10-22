# ============ Двухмерный анализ ========
# Иследование взаимодействий двух переменных(столбцов) одновременно
#Типы пар переменных 
# Число + число - корреляция(Пирсона, Спирмен) - количество клиентов - чайвые, итоговой счет и чайвые
# категория + категория - таблица сопреженности и критерии xi - квадрат -> пол - выживаемость, класс - выживаемость
# категория + число - сравнение групп -> возраст и выживаемость

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

tips = sns.load_dataset("tips")
print(tips.shape) # просмотр размерности
print(tips.columns) # просмотр названия колонок


diamonds = sns.load_dataset("diamonds")
print(diamonds.shape)
print(diamonds.columns)


titanic = sns.load_dataset('titanic')
print(titanic.shape)
print(titanic.columns)


colifornia = fetch_california_housing(
    as_frame=True
)
housing = colifornia.frame
print(housing.shape)
print(housing.columns)



# -------- Число + Число \ кореляция -----
# Корреляция - связь между двумя числовыми перменными. и сила направление Линейной(Пирсон) или монотонной(Спирмен) связи. Обозначается буквой r
# r = |-1| |1|
# 0 - нету связи
# 0.1 - 0.4 - слабая связь
# 0.4- 0.7 - умеренная
# 0.7 - 0.9 - сильная
# 1 - идеальная связь


#Пирсон
""" 
r = сумма(Xi-Xср)(Yi - Yср)/ корень(сумма(Xi-Xcр)**2 * сумма(Yi-Yср)**2)
Чуствителен к выбросам и видит только линейную связь
"""

# Спирмен
""" 
[1, 2, 3, 4, 5]- [1, 2, 3, 4, 5]
[10, 20, 30] - [1, 2, 3]
[200, 100, 300] - [2, 1, 3]
"""


from scipy import stats

r_p, p_p = stats.pearsonr(
    tips['total_bill'],
    tips['tip']
)
# r_p - сила связи
# p_p - p_value - значимость связи
print("Пирсон", r_p, p_p)

r_s, p_s = stats.spearmanr(
    tips['total_bill'],
    tips['tip']
)
print("Спирмен", r_s, p_s)

#Матрица корреляции и тепловая карта
matrix1 = tips.select_dtypes(
    include='number'
).corr()
print(matrix1.round(2))

print(tips.head())

dcorr_m = diamonds.select_dtypes(
    include='number'
).corr()
plt.figure(
    figsize=(10, 8)
)
sns.heatmap(
    dcorr_m, # Матрица корреляции
    annot=True, # Писать число внутри клетки
    cmap='RdBu_r', # Цветовая схема
    center=0, # середина шкалы
    vmin=-1, # нижняя граница
    vmax=1, # верхняя граница
    square=True, # клетки квадратные
    linewidths=0.5 # линия между клетками
)
plt.title("Корреляция")
plt.tight_layout() # убирает лишние поля
plt.savefig("eda_lections/diamond_heatmap.png")
#!!!!!!Корреляция не всегда равно причина-следствие!!!!!!

# СНАЧАЛА ГРАФИК - ПОТОМ СТАТИСТИКА
plt.figure(figsize=(8,6))
sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    alpha=0.6
)
plt.xlabel('Сумма счета')
plt.ylabel("чаевые")
plt.savefig("eda_lections/tips_scatter.png")

sns.lmplot(
    data=tips,
    x='total_bill',
    y='tip',
    height=6,
    aspect=1.3,
    scatter_kws={'alpha': 0.5},
    line_kws={'color':'red'}
)
plt.title('Линия тренда')
plt.savefig('eda_lections/tips_lmplot.png')


sns.scatterplot(
    data=tips,
    x = 'total_bill',
    y='tip',
    style='sex',
    hue='time',
    alpha=0.6
)
plt.title('Разбивка по категориям')
plt.savefig('eda_lections/tips_scatter_hue.png')


ancombe = sns.load_dataset('anscombe')
grafic = sns.lmplot(data=ancombe,
                    x='x',
                    y='y',
                    col='dataset', # отдельный график на группу
                    col_wrap=2, # по 2 подграфика в ряду
                    height=3.5,
                    aspect=1.2,
                    scatter_kws={'alpha': 0.7}
)

grafic.figure.suptitle("Квартет Анскомба", y=1.02)
plt.savefig('eda_lections/anscombe.png')