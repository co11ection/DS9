from base import Product, FoodProduct

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

    def add_product(self):
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
            self.create_product(product)
        except ValueError:
            print("Ошибка ввода")