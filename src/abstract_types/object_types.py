from abc import ABC
from .global_interfaces import IAlive, IInventory

class Animal(ABC, IAlive, IInventory):
    def __init__(self, food_amount, animal_id, number):
        self._food = food_amount
        self._id = animal_id
        self._number = number
    @property
    def Number(self):
        return self._number
    @Number.setter
    def Number(self, value):
        self._number = value
    @property
    def Id(self):
        return self._id
    @property
    def Food(self) -> int:
        return self._food
    @Food.setter
    def Food(self, value):
        self._food = value
    @property
    def Name(self):
        return self.__class__.__name__

class Thing(ABC, IInventory):
    def __init__(self, number):
        self._number = number
    @property
    def Number(self):
        return self._number
    @Number.setter
    def Number(self, value):
        self._number = value