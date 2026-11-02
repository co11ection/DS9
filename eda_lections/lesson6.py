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