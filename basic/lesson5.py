# Тип bool
# bool - True/False(истина/ложь)
# Операторы сравнения:

#  == - проверяет равенства
print(5 == 3) #False
print(5==5) #True

# != - не равно
print(5 != 3) #True
print(5!=5) #False
# > - больше
# < - меньше
# >= - больше или равно
# <= - меньше или равно

print('apple' == 'Apple')
print('apple' < 'apple1')
print(1 == True)
print(0 == False)

# print(0.000003 + 0.000002)


# if <условие>:
    # <тело1(код) которое доложно выполниться>
# elif <условие>:
    # <тело3(код) которое доложно выполниться>
# elif <условие>:
    # <тело3(код) которое доложно выполниться>
# else: 
    # <тело2(код) которое доложно выполниться>
    

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Совершеннолетний")
# else:
#     print("Несовершеннолетний")
    
score = 75
if score > 80:
    print(5)
elif score > 70:
    print(4)
elif score > 50:
    print(3)
else:
    print(2)

#<условие 1> and <условие 2>  - оба условия должны быть True
# True    True  -- True
#False    True --- False
# True     False --- False
# False   False -- False

# <условие 1> or <условие 2> - хотя бы одно условие долждно выдать True
# True     True   --  True
# False    True   -- True
# True    False   -- True
# False   False  -- False    


score = 90
if score > 50 and score < 70:
    print(3)
elif score >= 70 and score < 90:
    print(4)
elif score >= 90:
    print(5)
else:
    print(2)
    
    
# Вложенные условия
num = 5
if num > 2:
    num += 1
    if num == 4:
        print(num)
    else:
        print("Условие не выполненно")
else:
    print("Условие не выполненно")

# Тернарные операторы - условные операторы в одну строчку
# <вывод если условие выдвет True> if <условие> else <вывод если условие выдает False>
age = 10
status = "Взрослый" if age >= 18  else "Подросток" if age > 14 else "Ребенок"
print(status)