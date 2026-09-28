# ================ Seaborn ==============
# Это сторонняя библиотека, используется для визуализации, отличие от maplotlib в том что seaborn принимает dataframe(табличные данные)

import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd

data = {
    "category": ["Техника", "Аксессуары", "Техника", "Аксессуары",],
    "price": [120000, 50000, 160000, 30000]
}

df = pd.DataFrame(data)
# sns.barplot(data=df, x="category", y='price')
# plt.title("Цена по категориям")
# plt.show()


# hisplot, scatterplot

data = {
    "price": [55000, 2000, 800, 320000, 1200, 9800],
    "quantity": [2, 10, 5, 3, 4, 8]
}
df = pd.DataFrame(data)
# sns.histplot(data=df, x='price', bins=5)
# plt.title("Распределение цен")
# plt.show()

# sns.scatterplot(data=df, x='price', y='quantity')
# plt.title("Цена и колличество")
# plt.show()


# barplot
# sns.barplot(data=, x=, y=)

data = {
    "courses": ['DS', "DA", "DE", "MA", 'DS'],
    "groups": ['DS9', "DA10", "DE2", "MA1", "DS9"],
    "score": [85, 89, 78, 60, 100]
}

df = pd.DataFrame(data)

# sns.barplot(data=df, x='courses', y='score', hue='groups')
# plt.show()


# Создать DF со столбцами category, quantity (3 значения и каждая категория должна повторяться как минимум 2 раза) и построить barplot
# добавить месяц и вывести
data = {
    'category': ['Мобилка', 'Наушники', 'Зарядка', 'Мобилка', 'Наушники', 'Зарядка'],
    'quantity':[10, 15, 20, 13, 50, 40],
    "month": [1, 1, 1, 2, 2, 2]
}

df = pd.DataFrame(data)
# sns.barplot(data=df, x='category', y='quantity', hue="month")
# plt.show()


#boxplot lineplot


data = {
    "price": [55000, 2000, 800, 320000, 1200, 9800],
    "category": ["Техника", "Аксессуары", "Техника", "Аксессуары", "Техника", "Аксессуары",],
}
df = pd.DataFrame(data)

# sns.boxplot(data=df, x='category', y='price')
# plt.show()
data = {
    'quantity':[10, 15, 20, 13, 50, 40],
    "month": [1, 1, 1, 2, 2, 2]
}

df = pd.DataFrame(data)
# sns.lineplot(data=df, x='month', y='quantity')
# plt.show()


# Стили, размеры и сохранение графиков

sns.set_style('darkgrid')

data = {
    'category': ['Мобилка', 'Наушники', 'Зарядка', 'Мобилка', 'Наушники', 'Зарядка'],
    'quantity':[10, 15, 20, 13, 50, 40],
    "month": [1, 1, 1, 2, 2, 2]
}
df = pd.DataFrame(data)

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
sns.barplot(data=df, x='category', y='quantity', hue="month", palette='pastel', ax=axes[0])
axes[0].set_title("Столбчатая таблица")

sns.boxplot(data=df, x='category', y='quantity', ax=axes[1])
axes[1].set_title('Разброс значений')

plt.savefig('report.png')
plt.show()