from abc import ABC, abstractmethod
from interfaces import IAlive, IInventory

class Animal(ABC, IAlive):
    pass
class Herb(Animal):
    @property
    @abstractmethod
    def kindness_power(self):
        pass
class Predator(Animal):
    pass
class Thing(IInventory):
    pass
