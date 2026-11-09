#============== Автоматизированный EDA отчет ============
#sweetviz - библиотека для автоматизированного анализа\отчета

""" 
строит визуальный отчет
показывает распределение
выевляет пропуски
сравнивает датасеты
находит зависимости между признаками
"""
import seaborn as sns
import sweetviz as sv

df = sns.load_dataset('titanic')

print(df.head())
print(df.shape)

# Полноценный анализ
# report = sv.analyze(df)
# report.show_html("titanic_report.html")

# Анализ с таргетом
# report = sv.analyze(df, target_feat='survived')
# report.show_html('titanic_target.html')


# df = df.drop(columns=['adult_male'])
# male = df[df['sex'] == 'male']
# female = df[df['sex'] == 'female']
# report = sv.compare([male, "Мужчины"],[female, "Женщины"])
# report.show_html("titanic_compare.html")

# выборочный анализ 
report = sv.analyze(
    df[['age', 'fare', 'pclass', 'survived']]
)
report.show_html('titanic_select.html')