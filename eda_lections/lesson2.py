import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("eda_lections/magazin_orders.csv") 
# plt.hist(df['price'], bins=10)
# plt.title("Распределение цен")
# plt.savefig('eda_lections/price_distribution.png')


# sub = df[df['price']< 50000]['price']
# plt.hist(sub, bins=10)
# plt.title("Распределение цен без выбросов")
# plt.savefig('eda_lections/price_sub.png')



# работаем с quantity выводим выбросы методом IQR  рисум boxplot
qty = pd.to_numeric(df['quantity'], errors='coerce')
q1 = qty.quantile(0.25)
q3 = qty.quantile(0.75)
iqr = q3-q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = qty[(qty<lower)|(qty>upper)]
print(outliers)

# plt.boxplot(qty.dropna())
# plt.savefig("eda_lections/quantity.png")

# ----------- Асиметрия и log-преобразование ------
# 0 - идеальная симетрия
# <0.5 - почти симетрично
# 0.5-1 - умеренный скос
# 1 < - сильный скос
print(df['price'].skew())
clean_data = df[df['price']< 50000]['price']
print(clean_data.skew())

log_price = np.log1p(df['price'])
print(log_price.skew())

# print(df['price'].describe())
# print(df['price'].median())

qty = pd.to_numeric(df['quantity'], errors='coerce')
print(qty.skew())
log_qty = np.log1p(qty[qty<100])
print(log_qty.skew())


print(df['category'].value_counts())
print(df['category'].value_counts(normalize=True).round(3))
df['category'].value_counts().plot(kind='bar')
plt.ylabel('Количество')
plt.tight_layout()
plt.savefig("eda_lections/bar.png")