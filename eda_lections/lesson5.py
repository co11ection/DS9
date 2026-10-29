#===== Очистка данных и контроль качества ======
""" 
1) Никогда не перезаписывать исходный файл и не чистить df на месте без копии
2) Для каждого изменения фиксируйте что было сдделано и какое решение было принято
3) Сначала посчитать сколько проблема затрагивает и только после решать (3 из 146 и 90 из 146 имеет разницу)
"""
import pandas as pd
import numpy as np

df_raw = pd.read_csv(
    'eda_lections/magazin_orders.csv'
)
df = df_raw.copy()
print(df.shape) #(146, 10)

print(df.isna().sum())
#city            7
#rating         26


# dropna() - без аргументов удаляет каждую строку в котором есть пропуск - на правктике считается слишком агресивным
# dropna(subset=['column_name', ...]) - таким способом мы удаляем только в случае если пропуск имеется в указанных сстолбцах

#filna(значение) - заполняем пропуски mean/mediana/mode
df = df.dropna(
    subset=['city']
)
print("Строк после применения метода dropna", len(df))
#Строк после применения метода dropna 139

df["rating_was_missing"] = df['rating'].isna()

median_rating = df['rating'].median()
print('медиана rating', median_rating)
#медиана rating 4.0
df['rating'] = df['rating'].fillna(
    median_rating
)
print(df)
print("Пропуски rating", df['rating'].isna().sum())
#Пропуски rating 0

df_raw = pd.read_csv(
    'eda_lections/magazin_orders.csv'
)

print("Сумма дубликатов", df_raw.duplicated().sum())
#Сумма дубликатов 4

print("Дубликаты по order_id", df_raw['order_id'].duplicated().sum())
#Дубликаты по order_id 6

ids = df_raw["order_id"]

dup_rows = df_raw[
    ids.duplicated(keep=False)
][['order_id', 'city', 'price']].sort_values("order_id")
print(dup_rows)

before = len(df_raw)
print("Было строк", before)

df = df_raw.drop_duplicates(
    subset=['order_id', 'price', 'order_date'],
    keep='first'
)
print('удалено', before - len(df))
#Было строк 146
#удалено 6

print(df_raw['quantity'].unique())

try:
    pd.to_numeric(
        df_raw["quantity"]
    )
except ValueError as e:
    print(e)
    
qty_coerced = pd.to_numeric(
    df_raw['quantity'],
    errors='coerce'
)
print(qty_coerced)
bad_mask = qty_coerced.isna()
print(bad_mask.sum())
# Не распознанно 4

print(df_raw.loc[bad_mask, 'quantity'].unique())
#['н/д', 'одна шт', 'три', 'два']

text_to_number = {
    "н/д": np.nan,
    "одна шт": 1,
    "три": 3,
    "два": 2
}
qty_fixed = df_raw['quantity'].replace(text_to_number)
qty_fixed = pd.to_numeric(qty_fixed, errors='coerce')
print(qty_fixed.isna().sum())
print(qty_fixed.describe())

# Выбросы:
""" 
Три способа обработки выбросов:
1) удалить строку(в случае если это явная ошибка либо строка бесполезна)
2) Отсечь значение (capping\clipping - заменяем на границы допустимого диапазона, саму строку оставляем)
3) Пометить флагом (оставить как есть но в новом столбце is_outlier пометить флагом для дальнейшего анализа)

Series.clip(lower=..., upper =...)
границы обычно берутся с правила IQR - (Q1-1,5*IQR) -- (Q3+1,5*IQR)
"""
q1, q3 = df_raw['price'].quantile([0.25, 0.75])
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5* iqr
print((df_raw['price']>upper).sum())
# выше верхней границы 2 строки
price_clipped = df_raw['price'].clip(
    upper=upper
)
print(df_raw['price'].max())
print(price_clipped.max())
"""
125000.0
6168.568749999999
"""
# price == 0
print(
    (df_raw['price'] == 0).sum()
)
zero_price = df_raw['price'] == 0
print(df_raw.loc[zero_price, ['order_id', 'product', 'price']])

print(lower)
print((df_raw['price'] == 0).sum())
print(df_raw.loc[df_raw['price'] == 0, ['order_id', 'price']])
df_raw.loc[df_raw['price'] == 0, 'price'] = df_raw['price'].mean()
print(df_raw.loc[df_raw['order_id'] == 1123, ['order_id', 'price']])
print((df_raw['price'] == 0).sum())

# Категории
print(df_raw['city'].value_counts(dropna=False))

city_norm = df_raw['city'].str.strip().str.lower()
print(df_raw['city'].nunique())
print(city_norm.nunique())
city_map = {
    "екатеринбург": "Екатеринбург",
    "новосибирск": "Новосибирск",
    "санкт-петербург": "Санкт-Петербург",
    "москва": "Москва",
    "казань": "Казань"
}
df_raw['city'] = city_norm.map(
    city_map
)
print(df_raw['city'].value_counts(dropna=False))