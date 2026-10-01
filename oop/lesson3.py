# =================== Полиморфизм =====================
# Это когда в нескольких классах одинаково названные методы выполняют разные функционалы

# print(4+5)
# print("4"+"5")

class Dog:
    def make_sound(self):
        print("Гав Гав")

class Cat:
    def make_sound(self):
        print("Мяу Мяу")
        
dog1 = Dog()
cat1 = Cat()


print(dog1.make_sound())
print(cat1.make_sound())


print(len("hello world"))# Считает количество символов
print(len([1, 2, 3, 4])) # Считает количество элементов
print(len({'a': 2, "b": 3})) #Считает количество пар

# Создать три независимых класса Круг, Квадрат и Триугольник 
# С нужными размерами и с методом area() который вычисляет площадь
# круг pi* R **2
# a ** 2
# 0.5 * base * height

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
    
class Square:
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2
    

class Tringle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
    
    
c1 = Circle(4)
s1 = Square(3)
t1 = Tringle(3, 4)

print(c1.area())
print(s1.area())
print(t1.area())


# Связь наследования и полиморфизма

class Animal:
    def make_sound(self):
        print("Издает звук")
        

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Гав Гав")

class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        print("Мяу Мяу")
        
dog1 = Dog()
cat1 = Cat()


print(dog1.make_sound())
print(cat1.make_sound())
