# ================ Наследование ================
# Наследование - способ который позволяет нам создовать новый класс(дочерний класс,
# потомок, subclass) на основе существуещего класса(родительский, базовый, superclass)
# берет от него все его методы и атрибуты

#синтаксис
# class A:
#     def __init__(self, a):
#         self.a = a
        

# class B(A):
#     def __init__(self, a):
#         super().__init__(a)



class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def speak(self):
        return f"{self.name} издает звук"
    
    def info(self):
        return f"{self.name}, возраст {self.age}"
    

class Dog(Animal):
    def __init__(self, name: str, age: int, legs: int):
        super().__init__(name, age)
        self.legs = legs
    
    def speak(self):
        return f"{self.name} издает звук: Гав Гав!"
        
# super() -> обращение к родительскому классу


barsik = Dog('barsik', 2, 4)
print(barsik.name)
print(barsik.speak())
print(barsik.info())
    


# super()
class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def speak(self):
        print(f"{self.name} издает звук")
    
    def info(self):
        return f"{self.name}, возраст {self.age}"
    

class Dog(Animal):
    def __init__(self, name: str, age: int, legs: int):
        super().__init__(name, age)
        self.legs = legs
    
    def speak(self):
        super().speak()
        print("Гав Гав!")

class Cat(Animal):
    pass
        
barsik = Dog('barsik', 2, 4)
print(barsik.name)
print(barsik.speak())
print(barsik.info())

pifagor = Cat('pifagor', 1)
print(pifagor.speak())


# ============= Типы наследования ==================
#1) Одиночное наследование - дочерний класс наследуется от одного родительского класса
class Transport:
    def __init__(self, brand):
        self.brand = brand
        

class Car(Transport):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


#2 Мнодествоенное наследование - дочерний класс наследуется от нескольких родительских классов

class Flyable:
    def fly(self):
        return "может летать"
    
class Swimmable:
    def swim(self):
        return "Умеет плавать"
    

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Кря!"
    

duck = Duck()
print(duck.quack())
print(duck.swim())
print(duck.fly())
    

# Многоуровневое наследование:
# A(самый первый род класс) -> B(A) -> дочерний класс C(B)

class Animal:
    def live(self):
        return 'Жить'
    
class Mammal(Animal):
    def feed_milk(self):
        return "Кормит молоком"
    
    # def live(self):
    #     return "жить на пастбище"

class Cow(Mammal):
    def speak(self):
        return 'muuuu'

cow = Cow()
print(cow.speak())
print(cow.feed_milk())
print(cow.live())

# Ирархичное наследование
# у родительского класса несколько дочерних класссов

class Animal:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def speak(self):
        print(f"{self.name} издает звук")
    
    def info(self):
        return f"{self.name}, возраст {self.age}"
    

class Dog(Animal):
    def __init__(self, name: str, age: int, legs: int):
        super().__init__(name, age)
        self.legs = legs
    
    def speak(self):
        super().speak()
        print("Гав Гав!")

class Cat(Animal):
    pass


# =========== Проблема ромба ========
class A:
    def a(self):
        return 'a'


class B(A):
    def b(self):
        return "b"


class C(A):
    def c(self):
        return 'c'
    

class D(C, B):
    def d(self):
        return 'd'
    

d1 = D()
print(d1.a())
# MRO - method resolution order
print(D.__mro__)

