# =============== Matplotlib ============
""" 
Визуализация данныз - процесс преоброзования числовой информации
в графическую форму

Для чего:
1) быстрое понимание данных
2) находить закономерности
#) обьяснять другим результаты

сначала данные ---> визуализация(matplotlib) -----> оформление

"""

from matplotlib import pyplot as plt

# =================== Линейный график =================
""" 
x - значение времени или индекса
y - за само значение (прибль, температура)

для списков должна быть одинаковой
"""
# x = [1, 2, 3, 4, 5]
# y = [12, 14, 20, 22, 25]
# plt.plot(x, y)
# plt.title("Линейный график")
# plt.xlabel("Месяца")
# plt.ylabel("Температура")
# plt.show()

""" 
================== Точечный график ==========
"""
x = [1, 2, 3, 4, 5]
y = [12, 14, 20, 22, 25]

# plt.scatter(x, y)
# plt.title("Точечный грфик")
# plt.show()


# ======= Столбчатая диаграмма ==========
categories = ["A", "B", "C"]
values = [10 , 20, 30]

# plt.bar(categories, values)
# plt.show()


# ========= Гистограмма ==========
import numpy as np

# data = np.random.rand(1000)
# print(data)
# plt.hist(data, bins=100)
# plt.show()


# ============= Круговая диаграмма =============
#labels - подписи(название)
# seze - значение (размерность)

size = [40, 50, 100]
lables = ["BMW", "Mersedes", "Toyota"]

# plt.pie(size, labels=lables, autopct='%1.1f%%')
# plt.show()

""" 
color - цвет
linestyle - тип линии
marker - точки
"""

# x = [1, 2, 3, 4, 5]
# y = [12, 14, 20, 22, 25]
# plt.plot(x,y, color='red', linestyle='--', marker="o")
# plt.grid(True) # Сетка
# plt.show()


# Легенда
#legend - обьесняет какая линия что означает

# plt.plot(x, y, label="Линия")
# plt.legend()
# plt.show()



# ======== Практика ========
# Постройте линейный график y=x^2 для x от 1 до 10
# 1)
# x = list(range(1,11))
# y = [i**2 for i in x] 
# plt.plot(x, y)
# plt.show()

# 2) 
# x = np.arange(1, 11)
# y = x ** 2
# plt.plot(x, y)
# plt.show()


# Создать столбчатую диаграмму продаж
""" 
Пн : 10
Вт: 30
Ср : 5
"""
day = ["Пн", "Вт", "Ср"]
sales = [10, 30, 5]

plt.bar(day, sales)
plt.show()

""" 
Построить графика из 2 линий
# y = x 
# y = x**2
добавить легенду каждой линии
"""
x = np.arange(1, 11)
y1 = x
y2 = x ** 2

plt.plot(x, y1, label="y =x", color='blue') 
plt.plot(x, y2, label="y =x ** 2", color='red')

plt.legend()
plt.show() 