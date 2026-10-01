#============= Абстракция ================
# Нужна для правильной постройки классов (пользователь видит только главное а все остальное находится  в абстракции), так же для правильности Полиморфизма

# ПРАВИЛО: ЕСЛИ НАСЛЕДОВАЛСЯ ОТ АБСТРАКТНОГО КЛАССА ВСЕ МЕТОДЫ НУЖНО ПЕРЕОПРЕДЕЛЯТЬ!!!!
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2
    
ci = Circle(10)
print(ci.radius)
print(ci.area())



# class Shape:
#     def area(self):
#         pass


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
        
#     # def area(self):
#     #     return 3.14 * self.radius ** 2
    
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
        
#     def area(self):
#         return self.side ** 2
    
# ci = Circle(10)
# print(ci.radius)
# # print(ci.area())