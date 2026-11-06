# ======== Подготовка признаков на основе EDA ========
"""
Признак - это столбец, в котором хранится информаци я в понятном для модели(числа либо булевое значение)

Три группы техники для создания признаков:
1) Числовые преоброзование - стандартизация: меняем масштаб и форму числового столбца

2) Кодирование категорий - превращаем текст в числа

3) Производные признаки - комбинирование столбцов, агрегаты по группас что означает что мы создаем новую информацию из существующих столбцов

"""

import pandas as pd
import numpy as np

def clean_magazin_orders(df_raw: pd.DataFrame):
    df = df_raw.copy()
    report = {"rows_count_before": len(df)}
    
    city_map = {
        "екатеринбург": "Екатеринбург",
        "новосибирск": "Новосибирск",
        "казань": "Казань",
        "санкт-петербург": "Санкт-Петербург",
        "москва": "Москва"
    }
    
    df['city'] = (
        df['city'].str.strip().str.lower().map(city_map)
    )
    
    text_map = {
        "одна шт": 1,
        "два": 2,
        "три": 3,
        "н/д": np.nan
    }
    qty = pd.to_numeric(
        df["quantity"].replace(text_map)
    )
    bad_qty = (qty<1)|(qty>10)
    report['quantity_flagged'] = int(bad_qty.sum())
    qty["bad_qty"] = np.nan
    df['quantity'] = qty
    
    before = len(df)
    df = df.drop_duplicates(
        subset = ["order_id", "price", "order_date"],
        keep="first"
    )
    report["duplicate_removes"] = before - len(df)
    
    df['rating_is_missed'] = df['rating'].isna()
    df['rating'] = df["rating"].fillna(df["rating"].median())
    
    
    q1,q3 = df_raw['price'].quantile([0.25, 0.75])
    upper = q3 + 1.5 * (q3-q1)
    
    df['price_is_zero'] = df['price'] == 0
    
    report["pice_capped"] = int((df['price'] > upper).sum())
    
    df['price'] = df['price'].clip(upper=upper)
    report['row_after'] = len(df)
    return df, report

df_raw = pd.read_csv('eda_lections/magazin_orders.csv')
df_clean, report = clean_magazin_orders(df_raw)
print(report)
print(df_clean)


# =============== Числовые признаки: Распределение, log, стандартизация==========
""" 
Скошенное распределение - длинный хвост в одну сторону, в нашем случае price скошен вправо
так как большенство заказов недорогие, но и есть редкие дорогие заказы

log1p(x) = log(x+1) - сжимает большие значение сильнее чем маленькие, это способ для уменьшения правой скошенности, как у наших цен

Стандартизация(Z-SCORE): (x - среднее)/стандартное отклонение - приводит признак к среднему 0 и стандартному отклонению 1. Нужна для моделей которые чуствительны к масштабу


"""

print('skew price', round(df_clean['price'].skew(), 3))
#skew price 1.056 - заметная правая скошенность


df_clean['price_log'] = np.log1p(
    df_clean["price"]
)

print(
    "skew price log", round(df_clean['price_log'].skew(), 3)
)
# skew price log -2.17 --- стало хуже

nonzero = df_clean.loc[
    ~df_clean['price_is_zero'], "price" # ~ - логическое НЕ: берем все кроме price = 0
]
print('skew log1p withou price_is_zero', round(np.log1p(nonzero).skew(), 3))
#skew log1p withou price_is_zero -0.102


mean = df_clean["price_log"].mean()
std = df_clean['price_log'].std(
    ddof=0 # Делаить на N-колличество, а не на N-1
)

df_clean['price_log_z'] = (df_clean['price_log'] - mean) / std
print(df_clean['price_log_z'].describe().round(3))

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

z_sklearn = scaler.fit_transform(
    df_clean[['price_log']] 
)
print(z_sklearn)
print("Совпадает ли ручное решение с автоматическим",
    np.allclose(
        df_clean["price_log_z"], z_sklearn.ravel()
    )
)

# Биннинг: превращаем число в категорию

""" 
Биннинг - разбиение непревноего числового признакка на интервалы

pd.qcut('столбец', q=N) - деление на бины, границы считаются автоматически по квантилям

"""

price_quantile = pd.qcut(
    df_clean["price"],
    q=4,
    labels=['low', 'medium', 'high', 'premium']
)
print(price_quantile.value_counts())
""" 
price
low        35
medium     35
high       35
premium    35
"""

df_clean['price_bucket'] = pd.cut(
    df_clean["price"],
    bins = [-0.01, 1000, 3000, 10000],
    labels=['бюджетный', "средний", "дорогой"]
)
print(df_clean[["order_id", 'price', 'price_bucket']])
print(df_clean["price_bucket"].value_counts())

print(df_clean['order_date'].dtype)
df_clean['order_date'] = pd.to_datetime(
    df_clean["order_date"]
)
print(df_clean['order_date'].dtype)

df_clean['order_month'] = df_clean['order_date'].dt.month
df_clean["order_dow"] = df_clean["order_date"].dt.dayofweek
df_clean['is_weekend'] = df_clean['order_dow'].isin([5,6])

print(df_clean[['order_id', "order_month", "order_dow", "is_weekend"]])

print(df_clean["is_weekend"].sum())

last_date = df_clean["order_date"].max()
print("Последня дата", last_date)
import datetime
today = datetime.datetime.now()

df_clean['days_scince_order'] = (
    today - df_clean["order_date"]
).dt.days
print(df_clean[['order_id', "order_date", "days_scince_order"]])


# ======== Кодирование категорий =============
""" 
One hot encoding - каждому новому уникальному значению создается новый столбец и передается 0/1 (false/true) pd.get_dummies()
Работает хорошо с НЕБОЛЬШИМ количесвом уникальных данных, если количество уникальных много то он просто создаст дополнительные столбцы

frequence encoding - заменяем категорию на долю частоты, с которой она встречается в данных 
"""

print(df_clean['category'].value_counts())
# category
# Еда            33
# Книги          32
# Электроника    28
# Одежда         26
# Спорттовары    21


df_onehot = pd.get_dummies(
    df_clean,
    columns=["category"],
    prefix="cat"
)
# print(df_onehot)

cat_columns = [c for c in df_onehot.columns if c.startswith('cat_')]
print(cat_columns)
print(len(cat_columns))



print(df_clean['city'].isna().sum())

df_clean['city_is_missing'] = df_clean['city'].isna()
df_clean["city"] = df_clean['city'].fillna(
    "Неизвестно"
)

city_freq = df_clean['city'].value_counts(
    normalize=True
)
print(city_freq.round(3))


df_clean['city_freq'] = df_clean['city'].map(
    city_freq
)

print(df_clean[["order_id", "city", "city_freq"]])



# ================== Производные признаки, агрегаты и утечка данных ======
""" 
Производный признак - новый столбец который хранит в себе одно из последующих (отношение, разность, комбинация)
"""
df_clean['price_per_item'] = (
    df_clean["price"] / df_clean['quantity']
)
print(df_clean['price_per_item'].isna().sum())

price_75 = df_clean['price'].quantile(0.75)
df_clean['is_high_value'] = df_clean["price"] > price_75
print(df_clean[['order_id', 'price', 'is_high_value']])


""" 
Агрегаты groupby().transform() - возвращает то же длины что и основной df
"""

df_clean['avg_price_by_city'] = df_clean.groupby(
    'city', observed=True
)['price'].transform('mean')
print(df_clean[['order_id', 'city', 'avg_price_by_city']])

df_clean['price_vs_avg_city_price'] = (
    df_clean['price']/df_clean['avg_price_by_city']
)
print(df_clean[['order_id', 'city', 'avg_price_by_city', "price_vs_avg_city_price"]])

""" 
Утечка данных - ситуация когда признак использует информацию, которая в реальной жизни предсказать не возможно (средняя цена по всем данным включая будущие данные), МОДЕЛЬ НА ОБУЧЕНИИ ВЫГЛЯДИТ ОТЛИЧНО, А НА ПРОДЕ ЛОМАЕТСЯ

Правило против утечки: Агрегаты по группас считаютсся только на обучающих выборках train, а к тестовой применяются уже готовые посчитанные на train значения
"""
from sklearn.model_selection import train_test_split

train, test = train_test_split(
    df_clean,
    test_size=0.2,
    random_state=42
)
print("train:", train, len(train))
print('test', test, len(test))

city_avg_train = train.groupby(
    'city', observed=True
)['price'].mean()
print(city_avg_train)


test_feature = test['city'].map(
    city_avg_train
)
print(test_feature.isna().sum())