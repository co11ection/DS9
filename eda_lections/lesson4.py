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
from statsmodels.stats.outliers_influence import variance_inflation_factor

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
# mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
# plt.figure(figsize=(12,10))
# sns.heatmap(
#     corr_matrix, mask=mask, annot=True,
#     fmt='.2f', center=0, square=True, cmap='RdBu_r'
# )
# plt.title("Толька нижняя часть")
# plt.tight_layout()
# plt.show()


#Нахождение высоких корреляций автоматический
corr_pairs = (
    corr_matrix.where(
        np.triu(
            np.ones_like(
                corr_matrix, dtype=bool
            ), k=1
        )
    ).stack().reset_index()
)
corr_pairs.columns = ['var1', 'var2', 'correlation']
corr_pairs['abs_corr'] = corr_pairs['correlation'].abs()

# print(corr_pairs)
top10 =  corr_pairs.nlargest(10, "abs_corr")
print(top10)

# ------------- Мультиколлинереальность -------
""" 
Это ситуация когда один признак можно предсказать по другим

например площадь м^2 и площадь в футах. Оно мешать нашей модели и искожает коэфиценты регресии

Модель не может разделить эфекты - если два признака почти оддинаковые, коэфицент становится не стабильным

Растет дисперсия оценок - p_value -> завышается, важные признаки становятся не значительными

Модель переобучается - лишние данные добавляется шум, но не сама информация

Обноружение VIF - показывает на сколько каждый признак предсказывается остальными

VIF = 1 - нет коллинериальности
VIF = 5-10 - умеренная
VIF > 10 сильная. нам нужно удалить признаки 
"""

# print(housing)
x = housing.drop("MedHouseVal", axis=1)

x_scaled = (x - x.mean())/x.std() # Стандартизация

VIF_data = pd.DataFrame({
    'feature': x_scaled.columns,
    'VIF': [variance_inflation_factor(x_scaled.values, i) for i in range(x_scaled.shape[1])]
}
)

print(VIF_data.sort_values('VIF', ascending=False))


# Pairplot - все пары в одном графике
"""
сетка графиков где кажда пара показана как scatter plot,
а диоганали распределение каждой переменной
 
"""
# print(iris.columns)
# sns.pairplot(
#     iris, hue='species', diag_kind='kde', plot_kws={"alpha": 0.6}
# )
# plt.title("Pairplot")
# plt.show()



# print(penguins)


# sns.pairplot(
#     penguins,
#     hue='species',
#     vars=[
#         'bill_length_mm',
#         'bill_depth_mm',
#         'flipper_length_mm',
#         'body_mass_g'
#     ],
#     diag_kind='kde', palette='Set2',
#     plot_kws={'alpha': 0.5}
# )
# plt.show()



#Scaling
# Разные масштабы ломают алгоритм
""" 
Виды маштабирования
StandartScaler - среднее, дисперсия - почти всегда используется
MinMaxScaler - значения между [0,1] - для нейросетей, для картинок
RobutScaler - устойчив к выбросам 
"""

# ЕСЛИ НЕ ЗНАЕТЕ ЧТО БРАТЬ ТО БЕРЕМ StandartScaler

from sklearn.preprocessing import StandardScaler, MinMaxScaler

penguins_data = penguins[[
        'bill_length_mm',
        'bill_depth_mm',
        'flipper_length_mm',
        'body_mass_g']]
standart = StandardScaler()

penguins_scalled = standart.fit_transform(
    penguins_data
)
print(penguins_scalled)

penguins_df = pd.DataFrame(penguins_scalled, columns=penguins_data.columns)
print(penguins_df)
print(penguins_df.describe())