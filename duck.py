from abc import ABC, abstractmethod

class Duck(ABC):
    def __init__(self, fly_behavior, quack_behavior, display_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior =  quack_behavior
        self.display_behavior =  display_behavior
    
    def fly(self):
        self.fly_behavior.fly()

    def set_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def quack(self):
        self.quack_behavior.quack()


    def display(self):
        self.display_behavior.display()




class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyCloud(FlyBehavior):
    def fly(self):
        print("fly")


class FlyNone(FlyBehavior) :
    def fly(self):
        print("don't fly")

class FlyDry(FlyBehavior) :
    def fly(self):
        print("fly dry")



class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass

class QuackLoud(QuackBehavior):
    def quack(self):
        print("QUACK")
        
class QuackNot(QuackBehavior):
    def quack(self):
        print("....")


class DisplayBehavior(ABC):
    @abstractmethod
    def display(self):
        pass

class DisplayReal(DisplayBehavior):
    def display(self):
        print("i'am real")

class DisplayNotReal(DisplayBehavior):
    def display(self):
        print("i'am not real")



class MallardDuck(Duck):
    def __init__(self):
        super().__init__(fly_behavior=FlyCloud(), quack_behavior=QuackLoud(), display_behavior=DisplayReal())


class RedHeadDuck(Duck):
    
    def __init__(self):
        super().__init__(fly_behavior=FlyDry(), quack_behavior=QuackLoud(), display_behavior=DisplayReal())   
        

class RubberDuck(Duck):
    
    def __init__(self):
        super().__init__(fly_behavior=FlyNone(),quack_behavior=QuackNot(), display_behavior=DisplayNotReal())
        

if __name__ == '__main__':
    donald = MallardDuck()
    picsou = RedHeadDuck()
    rubber = RubberDuck()
    donald.fly()
    picsou.fly()
    rubber.fly()

    picsou.set_behavior(FlyCloud())
    picsou.fly()

    donald.quack()
    picsou.quack()
    rubber.quack()

    donald.display()
    picsou.display()
    rubber.display()