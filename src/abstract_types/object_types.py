from abc import ABC
from .global_interfaces import IAlive, IInventory

class Animal(ABC, IAlive, IInventory):
    def __init__(self, food_amount, number):
        self._food = food_amount
        self._number = number
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self, value):
        self._number = value
    @property
    def food(self) -> int:
        return self._food
    @food.setter
    def food(self, value):
        self._food = value
    @property
    def name(self):
        return self.__class__.__name__

class Thing(ABC, IInventory):
    def __init__(self, number):
        self._number = number
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self, value):
        self._number = value