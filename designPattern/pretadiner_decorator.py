from abc import ABC, abstractmethod

class Beverage(ABC):
    
    def __init__(self, description, base_cost):
        self.__description = description

    @abstractmethod 
    def cost(self):
        pass
    
    @property
    def description(self):
        return self.__description
    
class Coffee(Beverage):
    
    def __init__(self):
        super().__init__('coffee')
        
class Latte(Beverage):
    
    def __init__(self):
        super().__init__('latte')
        
class Chocolate(Beverage):
    
    def __init__(self):
        super().__init__('chocolate')
        

class Ingredient(Beverage):
    def __init__(self, price, quantity, description):
        self.__price = price
        self.__quantity = quantity
        super().__init__(description=description)

    def cost(self):
        return self.__price * self.__quantity

class Milk(Ingredient):
    pass

class Sugar(Ingredient):
    pass

class Soja(Ingredient):
    pass

class CoffeeBeann(Ingredient):
    pass


if __name__ == '__main__':
    beverage_1 = Coffee()
    print(f'{beverage_1.description} : {beverage_1.cost()}')
    beverage_2 = Chocolate()
    print(f'{beverage_2.description} : {beverage_2.cost()}')