import pandas as pd
import numpy as np

def clean_magazin_orders(df_raw: pd.DataFrame):
    df = df_raw.copy()
    report = {"rows_count_before": len(df)}

    city_map = {
        "екатеренбург": "Екатеринбург",
        "новосибирск": "Новосибирск",
        "казань": "Казань",
        "санкт-петербург": "Санкт-Петербург",
        "москва": "Москва",
    }
    df['city'] = (
        df['city']
        .str.strip().str.lower().map(city_map)
    )

    text_map = {
        "одна шт": 1,
        "два": 3,
        "три": 3,
        "н/д": np.nan
    }
    qty = pd.to_numeric(
        df["quantity"].replace(text_map),
    )
    bad_qty = (qty<1) | (qty>10)
    report["quantity_flagged"] = int(bad_qty.sum())
    qty[bad_qty] = np.nan
    df['quantity'] = qty

    bafore = len(df)
    df = df.drop_duplicates(
        subset=['order_id', 'price', 'order_date'],
        keep='first'
    )
    report["duplicates_removes"] = bafore - len(df)

    df['rating_is_missed'] = df['rating'].isna()
    df['rating'] = df['rating'].fillna(df["rating"].median())


    q1,q3 = df_raw['price'].quantile([0.25, 0.75])
    upper = q3 + 1.5 * (q3 - q1)

    df['price_is_zero'] = df['price'] == 0

    report["price_capped"] = int((df['price'] > upper).sum())

    df['price'] = df['price'].clip(upper=upper)
    report["row_after"] = len(df)
    return df, report

df_raw = pd.read_csv('eda_lections/magazin_orders.csv')
df_clean, report = clean_magazin_orders(df_raw)
print(report)
print(df_clean)


# ============= Числовые признаки : Распределение , log, стандартизация =============
"""
Скошенное распределение - длинный хвост в одну сторону, в нашем случае price скоени вправо
так как большинство заказов недорогие, но и есть редкие дорогие заказы

log1p(x) = log(x+1) - сжимает большие значение сидьнее чем маленькие, это способ для уменшение правой скошености, как у наших цен

Стандартихация (z-score): (x - среднее) / стандартное отклонение - приводит признак к среднему 0 и стандартному отклонению 1. Нужна для моделей которые чуствительны к масштабу признаков, например линейные модели, нейронные сети


"""

print("skew price", round(df_clean['price'].skew(), 3))
# skew price 1.056 - заметная правая скошеность


df_clean['price'] = np.log1p(
    df_clean['price']
)

print(
    "skew price log", round(df_clean['price'].skew(), 3)
)
# skew price log -2.17 - стало хуже

nonzero = df_clean.loc[
    ~df_clean['price_is_zero'], 'price' # ~ - логическая НЕ: берем все кроме price=0
]
print('skew log1p withou zero', round(nonzero.skew(), 3))