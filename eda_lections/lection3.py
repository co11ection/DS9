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
from scipy import stats

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


# from scipy import stats

# r_p, p_p = stats.pearsonr(
#     tips['total_bill'],
#     tips['tip']
# )
# r_p - сила связи
# p_p - p_value - значимость связи
# print("Пирсон", r_p, p_p)

# r_s, p_s = stats.spearmanr(
#     tips['total_bill'],
#     tips['tip']
# )
# print("Спирмен", r_s, p_s)

#Матрица корреляции и тепловая карта
# matrix1 = tips.select_dtypes(
#     include='number'
# ).corr()
# print(matrix1.round(2))

# print(tips.head())

# dcorr_m = diamonds.select_dtypes(
#     include='number'
# ).corr()
# plt.figure(
#     figsize=(10, 8)
# )
# sns.heatmap(
#     dcorr_m, # Матрица корреляции
#     annot=True, # Писать число внутри клетки
#     cmap='RdBu_r', # Цветовая схема
#     center=0, # середина шкалы
#     vmin=-1, # нижняя граница
#     vmax=1, # верхняя граница
#     square=True, # клетки квадратные
#     linewidths=0.5 # линия между клетками
# )
# plt.title("Корреляция")
# plt.tight_layout() # убирает лишние поля
# plt.savefig("eda_lections/diamond_heatmap.png")
# #!!!!!!Корреляция не всегда равно причина-следствие!!!!!!

# # СНАЧАЛА ГРАФИК - ПОТОМ СТАТИСТИКА
# plt.figure(figsize=(8,6))
# sns.scatterplot(
#     data=tips,
#     x='total_bill',
#     y='tip',
#     alpha=0.6
# )
# plt.xlabel('Сумма счета')
# plt.ylabel("чаевые")
# plt.savefig("eda_lections/tips_scatter.png")

# sns.lmplot(
#     data=tips,
#     x='total_bill',
#     y='tip',
#     height=6,
#     aspect=1.3,
#     scatter_kws={'alpha': 0.5},
#     line_kws={'color':'red'}
# )
# plt.title('Линия тренда')
# plt.savefig('eda_lections/tips_lmplot.png')


# sns.scatterplot(
#     data=tips,
#     x = 'total_bill',
#     y='tip',
#     style='sex',
#     hue='time',
#     alpha=0.6
# )
# plt.title('Разбивка по категориям')
# plt.savefig('eda_lections/tips_scatter_hue.png')


# ancombe = sns.load_dataset('anscombe')
# grafic = sns.lmplot(data=ancombe,
#                     x='x',
#                     y='y',
#                     col='dataset', # отдельный график на группу
#                     col_wrap=2, # по 2 подграфика в ряду
#                     height=3.5,
#                     aspect=1.2,
#                     scatter_kws={'alpha': 0.7}
# )

# grafic.figure.suptitle("Квартет Анскомба", y=1.02)
# plt.savefig('eda_lections/anscombe.png')


# # ------------Категория + число ----------------
# # Отличие числа между разными категориямии
# # Первый шаг
# print(
#     tips.groupby(
#         'smoker', # Столбец по которому мы группируем
#         observed=True # без пустых комбинаций
#     )['tip'].agg(['mean', 'median', 'std', 'count']).round(3)
# )


# print(
#     tips.groupby(
#         'day',
#         observed=True
#     )['total_bill'].mean().round(2)
# )

# Шаг 2 - Визуализация

# Boxplot --> Универсальный вобор используется когда надо сравнить медиану, IQR и выбросынескольких групп
# Violin - Когда важна форма распределения
#swarm - Когда точека(данных) мало в группе(до 200) и нужно посмотреть на каждую точку
#Bar - используется для презентации , так как проще читается, но скрывает разбросы

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=tips,
    x='day',
    y='total_bill'
)
plt.title('Распределение суммы счета по дням')
# plt.savefig('eda_lections/tips_box.png')

plt.figure(figsize=(8, 5))
sns.violinplot(
    data=tips,
    x='day',
    y="total_bill"
)
plt.title('Форма распределения')
# plt.savefig("eda_lections/tips_violin.png")

plt.figure(figsize=(8, 5))
sns.swarmplot(
    data=tips,
    x = 'smoker',
    y='tip'
)
plt.title('Чаевые: курящие VS не курящие')
plt.savefig("eda_lections/tips_swarm.png")


# Категория + категория

cross_titanic = pd.crosstab(
    titanic['survived'],
    titanic['pclass'],
    normalize='columns'
) * 100
print(cross_titanic.round(1))



# Критерии X**2 ---- проверяет связаны ли две категориальные переменные друг от друга. Для этого сравнивается Наблюдаемые(O) данные с ожидаемыми(E)

""" 
X**2 = сумма(O - E)**2 / E
E = (сумма по строке * сумма по столбцу)/общее количество
p_value < 0.05 - переменные связаны
p_value >= 0.05 - переменные не связаны
(p_value >= 0.05 - Не означает связи нету, просто данные его не подтвердили)
"""
from scipy.stats import chi2_contingency
cross_titanic = pd.crosstab(
    titanic['survived'],
    titanic['pclass'],
) 
print(cross_titanic)

chi2, p_value, dof, expected = chi2_contingency(
    cross_titanic
)
print(f"""
chi2 = {chi2}
dof = {dof}
p_value = {p_value}
expected = {expected}
      """)



# -------- Статистические тесты для сравнения групп --------№
# Статистический тест отвечает на вопрос: различие между группами которые мы видим на графике, реально могло такое получиться или это случайность

# p_value - предпологаем что различий нету(назвается нулевой гипотезой)
# смотрим на сколько вероятно получить такие данные при этом предположении
""" 
p< 0.05 - маловероятно, различия считается стастистически значимыми
p>=0.05 - данные не дают отвергнуть что различий нету

Выбор теста зависит от двух вопросов
---------------------------------------------
Группа| данные нормальноые| тест
2     | да                | t-test
2     | нет               | Mann-Whitney U
3+    | да                | ANOVA
3+    | нет               | Kruskal-Wallis
---------------------------------------------
"""
smoker = tips[tips['smoker']=='Yes']['tip']
print('smoker count: ', len(smoker))

no_smoker = tips[tips['smoker']=='No']['tip']
print('no smoker count:', len(no_smoker))

_, p_s = stats.shapiro(
    smoker
)
#shapiro() - возвращает (статистику, p_value)
_, p_ns = stats.shapiro(
    no_smoker
)
print("Нормальность курящих:", f"{p_s:.2e}")
print("Нормальность не курящих:", f"{p_ns:.2e}")

# Так как оба p_value << 0.05 данные считаются не нормальными
# Поэтомы выбираем Mann-Whitney, а не t-test

u_stats, p_mw = stats.mannwhitneyu(
    smoker,
    no_smoker,
    alternative = 'two-sided'
)
print(f"MW U={u_stats:.1f}, p={p_mw:.4f}") #MW U=7163.0, p=0.7919


t_stats, p_t = stats.ttest_ind(
    smoker, no_smoker
)
print(f"t-test={t_stats:.4f}, p={p_t:.4f}")# t-test=0.0922, p=0.9266

groups = [
    g['total_bill'].values
    for _, g in tips.groupby('day', observed=True)
]

f_stats, p_anova = stats.f_oneway(
    *groups
)
print(f"ANOVA={f_stats:.4f}, p={p_anova:.4f}") #ANOVA=2.7675, p=0.0425


h_stats, p_kw = stats.kruskal(
    *groups
)
print(f"Kruskal-Wallis: {h_stats:.4f}, p={p_kw:.4f}") #Kruskal-Wallis: 10.4031, p=0.0154


