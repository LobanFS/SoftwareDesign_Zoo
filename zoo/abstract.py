from abc import ABC, abstractmethod
from interfaces import IAlive

class Animal(ABC, IAlive):
    pass;
class Herb(Animal):
    pass;