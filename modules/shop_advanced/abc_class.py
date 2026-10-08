from abc import ABC, abstractmethod

#------------------
# Абстрактный класс ProductBase
#------------------
class ProductBase(ABC):
    @abstractmethod
    def info(self):
        pass