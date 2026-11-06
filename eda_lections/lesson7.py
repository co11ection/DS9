# =============== Advanced EDA и диагностика ===========

import pandas as pd
import numpy as np
from scipy import stats

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


"""
Описсательный EDA - Распределение, пропуски и выбросф одного столбца
Реляционный EDA - Корреляция, группировка, один статистический тест
Диагностика EDA - задаемся вопросом: Почему наблюдаем тот или иной результат?
Сравниваем много групп сразу, Проверяем несколько гипотез и ищем скрытые искажающие картину третьи переменные
"""
#==== Многомерная агрегация =======
""" 
pd.pivot_table(
    df - наш датасет
    values - какой столбец надо агрегировать
    index - группировка по каким строкам
    aggfunc - какие агрегирующие функции использовать
)
стводная таблица  группирует на датасет по index и считает aggfunc для нашего столбца
"""
pivot_price = pd.pivot_table(
    df_clean,
    values='price',
    index='category',
    aggfunc=['mean', 'median', 'count', 'std']
)
# pivot_price_raw = pd.pivot_table(
#     df_raw,
#     values='price',
#     index='category',
#     aggfunc=['mean', 'median', 'count', 'std']
# )
print(pivot_price)
# print(pivot_price_raw)


pivot_price = pd.pivot_table(
    df_clean,
    values='price',
    index='category',
    columns='city',
    aggfunc=['mean'],
    observed=True
)
print(pivot_price)


# Сравнение 3+ групп
""" 
Если есть хоть какието сомнения по поводу нормальности данных, либо они проваливают проеврку
Шапиро то используем тест Kruskal-Wallis
"""
for cat, g in df_clean.groupby('category', observed=True):
    stat, p_norm = stats.shapiro(
        g['price']
    )
    print(cat, 'lenght', len(g), "shapiro p", round(p_norm, 4))
    

groups = [
    g["price"].values
    for _, g in df_clean.groupby(
        'category', observed = True
    )
]

h_stats, p_value = stats.kruskal(
    *groups
)
print("h=", h_stats, 'p_value', p_value)


sub = df_clean.dropna(subset=['city'])
for cit, g in sub.groupby('city', observed=True):
    stat, p_norm = stats.shapiro(
        g['price']
    )
    print(cit, 'lenght', len(g), "shapiro p", round(p_norm, 4))
    

groups = [
    g["price"].values
    for _, g in sub.groupby(
        'city', observed = True
    )
]

h_stats, p_value = stats.kruskal(
    *groups
)
print("h=", h_stats, 'p_value', p_value)



# ===========Диагностика ======
""" 
Систематическая диагностика - формулируем несколько гипотез о возможной причине явлении и проверяем каждую отдельным тестом
"""
#Гипотеза 1 (влияет ли категория на возврат)
ct_cat = pd.crosstab(df_clean['category'], df_clean["is_returned"])
print(ct_cat)

chi2, p_cat, dof, expexted = stats.chi2_contingency(
    ct_cat
)

print("chi2 p ", round(p_cat, 4))

# Гипотеза 2: влияет ли цена на возврат
returned= df_clean.loc[
    df_clean['is_returned'] == "Да", 'price'
]

not_returned= df_clean.loc[
    df_clean['is_returned'] == "Нет", 'price'
]

print(f"Возвраты: {len(returned)}, без возврата{len(not_returned)}")

u_stat, p_price = stats.mannwhitneyu(
    returned, not_returned,
    alternative='two-sided'
)
print(
    "Средняя цена возврата: ", round(returned.mean(), 1),
    "Средняя цена без возврата: ", round(not_returned.mean(), 1),
    "p=", round(p_price, 4)
     
)