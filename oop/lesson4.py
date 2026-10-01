# ======================= Инкапсуляция ==========================
# имеет две трактовки
# 1) Принцип который обьединяет атрибуты и методы одного обьекта
# 2) Принцип который занимается уровнями доступа
#   2.1) Публичный - доступен всем ---> radius, nickname
#   2.2) Защищенный доступ - доступно внутри класса и в дочерних классах но не используется вне класса ---> _phone_number, _name
#   2.3) Приватный доступ - Доступен только внутри основного класса ---> __balance, __password, __inn


class BankAccaunt:
    def __init__(self, username: str, card_number: int, balance: float = 0):
        self.username = username
        self._card_number = card_number
        self.__balance = balance
        
    def info(self):
        print(
            f"""
            Пользователь: {self.username}
            Номер карты: {self._card_number}
            Баланс: {self.__balance} 
            """
        )
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount: float):
        self.__balance += amount
    


aktan = BankAccaunt('aktan3000', 416958537456)
print(aktan.username)
# print(aktan._card_number) так делать нельзя
# print(aktan.__balance) Привытный не отображается
print(dir(aktan))
print(aktan._BankAccaunt__balance) # обходной путь защиты приватных атрибутов\методов

print(aktan.info())
print(aktan.get_balance())
print(aktan.deposit(120050.56))
print(aktan.deposit(120050.56))
print(aktan.get_balance())