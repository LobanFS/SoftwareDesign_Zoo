from abc import ABC
from .global_interfaces import IAlive, IInventory

class Animal(ABC, IAlive, IInventory):
    def __init__(self, *, food_amount: int, number: int, title:str = "NoTitle"):
        self._food = food_amount
        self._number = number
        self._title = title
    @property
    def number(self) -> int:
        return self._number
    @number.setter
    def number(self, value: int) -> None:
        self._number = value

    @property
    def food(self) -> int:
        return self._food
    @food.setter
    def food(self, value: int) -> None:
        self._food = value

    @property
    def name(self) -> str:
        return self.__class__.__name__

class Thing(ABC, IInventory):
    def __init__(self, number: int, title: str = "NoTitle"):
        self._number = number
        self._title = title

    @property
    def number(self) -> int:
        return self._number
    @number.setter
    def number(self, value: int) -> None:
        self._number = value

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def title(self):
        return self._title