

# LEGB
""" 
L - local локальный тоесть функция где мы находимся
E - enclosed функция которая находится поверх
G - global глобальный все внутри файла
B - built in встроенные имена Python (print, input, len, range)
"""

a = 5 # глобальныая переменнпя

def outer():
    #enclosed
    a = 4 # локадьная ---> для inner функции является enclosed
    def inner():
        #local
        a = 6 #локальный
        pass
# print(a) # built-in



num = 5
def outer():
    global num
    num += 1
outer()
print(num)

#---------------------------

def outer1():
    num = 1
    def inner():
        nonlocal num
        num+=10
    inner()
    print(num)
outer1()


num = 10
def outer1():
    global num
    num = 1
    def inner():
        global num
        num+=10
        def inner1():
            global num
            num+=10
        inner1()
    inner()

outer1()
print(num)



# Создать переменную balance = 1000 функция add_money(amount) 
# баланс должен увеличиваться
balance = 1000
def add_money(amount):
    global balance
    balance += amount
add_money(400)
add_money(200)
add_money(1200)
print(balance)

# у вас есть переменная temperature = 5
# одна функция увеличивает ее на 10
# а другая уменьшает на 5

temperature = 5

def first():
    global temperature
    temperature += 10
    
def second():
    global temperature
    temperature -= 5

first()
first()
first()
second()
second()

print(temperature)