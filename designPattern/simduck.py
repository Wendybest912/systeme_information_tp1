from duck_strategy import Duck, MallardDuck, RedHeadDuck, RubberDuck
from weatherstation_observer import Observer
from abc import ABC, abstractmethod

class Quakologist(Observer):
    def __init__(self, pseudo):
        self.pseudo = pseudo

    def notify(self, subject):
        return super().notify(subject)

class Goose():
    def honk(self):
        print("honk")
    
    def fly(self):
        print("Goosing")

class GooseAsDuck(Duck):
    def __init__(self, goose: Goose):
        self.__goose = goose

    def quack(self):
        self.__goose.honk()

    def fly(self):
        self.__goose.fly()


class duckSimulator:
    def simulate(self, duck:Duck):
        self.__fly_n_times(duck, 2)
        duck.quack()
        self.__fly_n_times(duck, 3)

    def __fly_n_times(self, duck, n_times):
        for _ in range(n_times):
            duck.fly()

class QuackCount(Duck):
    def __init__(self, duck: Duck):
        self.__duck = duck
        self.number_of_quacks = 0

    def quack(self):
        self.number_of_quacks += 1
        self.__duck.quack()

    def fly(self):
        self.__duck.fly()

    def display(self):
        self.__duck.display()  



if __name__ == '__main__':
    ducks = []
    ducks.append(QuackCount(MallardDuck()))
    ducks.append(QuackCount(RedHeadDuck()))
    ducks.append(QuackCount(RubberDuck()))

    goose = GooseAsDuck(Goose())

    sim_duck = duckSimulator()
    for duck in ducks:
        sim_duck.simulate(duck)
        print(duck.number_of_quacks)
    sim_duck.simulate(goose)
