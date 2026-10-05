from abc import ABC, abstractmethod

#------------------
# Абстрактный класс ProductBase
#------------------
class ProductBase(ABC):
    @abstractmethod
    def info(self):
        pass
    

#---------------
# Базовый класс Product
#---------------
class Product(ProductBase):
    def __init__(self, name, price, quantity, category):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__category = category
    
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def get_quantity(self):
        return self.__quantity
    
    def get_category(self):
        return self.__category
    
    
    def set_name(self, name):
        self.__name = name
        
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Цена должна быть выше 0")
            
    def set_quantity(self, quantity):
        if quantity > 0:
            self.__quantity = quantity
        else:
            print("количество должна быть не ниже 0")
            
    def set_category(self, category):
        self.__category = category
    
    
    def info(self):
        print(
            f"""
            Название: {self.__name}
            Цена: {self.__price}
            Количество: {self.__quantity}
            Категория: {self.__category} 
            """
        )
        

class FoodProduct(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity, "Еда")
        self.expiration_date = expiration_date
        
    
    def info(self):
        print(
           f"""
            Продукт питания
            Название: {self.get_name()}
            Цена: {self.get_price()}
            Количество: {self.get_quantity()}
            Срок годности: {self.expiration_date}
            """
        )

class Store:
    def __init__(self):
        self.products = []
    
    def create_product(self, product):
        self.products.append(product)
        print("Товар добавлен")
    
    def show_products(self):
        if not self.products:
            print("Товаров нету")
            return 
        print("----Товары---")
        for product in self.products:
            product.info()
            
    def find_product(self, name):
        for product in self.products:
            if product.get_name().lower() == name.lower():
                return product
        return None
    
    def update_product(self, name):
        product = self.find_product(name)
        
        if product is None:
            print("Продукта нету")
            return
        
        try:
            price = float(input("Введите Цену: "))
            quantity = int(input("Введите количество: "))
            
            product.set_price(price)
            product.set_quantity(quantity)
            
            print("Товар обновлен")
        except ValueError:
            print("Ошибка ввода")
            
    def delete(self, name):
        product = self.find_product(name)
        
        if product is None:
            print("Товар не найден")
            return
        
        self.products.remove(product)
        print("Товар удален")
        
    def sort_price(self):
        sorted_products = sorted(self.products, key=lambda product: product.get_price())
        
        for product in sorted_products:
            product.info()
    
    
    def sort_name(self):
        sorted_products = sorted(self.products, key=lambda product: product.get_name())
        
        for product in sorted_products:
            product.info()    
    
    def expensive_products(self):
        try:
            price = float(input("Введите минимальную цену: "))
        except ValueError:
            print("Ошибка ввода")
            return
        result = [product for product in self.products if product.get_price()> price]
        if not result:
            print("Нет товаров выше этой цены")
            return
        
        for produc in result:
            produc.info()
            
    def total_cost(self):
        total = sum(product.get_price() * product.get_quantity() for product in self.products)
        print(f"Общая сумма составляет: {total}")
    
    def total_quantity(self):
        total = sum(product.get_quantity() for product in self.products)
        print(f"Общее количество продуктов состовляет: {total}")


#============= Меню =============
store = Store()

MENU = """
1. Добавить товар
2. Показать товары
3. Изменить товар
4. Удалить товар
5. Поиск товара
6. Сортировка по цене
7. Сортировка по названию
8. Показать товары дороже заданной суммы
9. Показать общую стоимость склада
10. Показать общее количество товаров
0. Выход
"""

def add_product():
    print("1. Обычный товар")
    print("2. Продукт питания")
    
    product_type = input("Тип продукта: ")
    try:
        name = input("Название: ")
        price = float(input("Цена: "))
        quantity = int(input("Количество: "))
        
        if product_type == "1":
            category = input("Категория: ")
            product = Product(name, price, quantity, category)
        elif product_type == "2":
            expiration_date = input("Срок годности: ")
            product = FoodProduct(name, price, quantity, expiration_date)
        else:
            print("Выбран не верный тип продукта")
            return
        store.create_product(product)
    except ValueError:
        print("Ошибка ввода")


def main():
    while True:
        print(MENU)
        choice = input("Введите команду: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            store.show_products()
        elif choice == "0":
            print("Программа закрыто")
            break
        

if __name__ == "__main__":
    main()