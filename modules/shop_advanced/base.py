from abc_class import ProductBase
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