from abc import ABC
from src.abstract_types.global_interfaces import IAlive, IInventory

class Animal(IAlive, IInventory):
    def __init__(self, *, food_amount: int, number: int, title:str = "NoTitle"):
        if food_amount < 0: raise ValueError("food_amount must be >= 0")
        if number < 0: raise ValueError("number must be >= 0")
        self._food = food_amount
        self._number = number
        self._title = title

    @property
    def number(self) -> int:
        return self._number
    @number.setter
    def number(self, value: int) -> None:
        if value < 0: raise ValueError("number must be >= 0")
        self._number = value

    @property
    def food(self) -> int:
        return self._food
    @food.setter
    def food(self, value: int) -> None:
        if value < 0: raise ValueError("food must be >= 0")
        self._food = value

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def title(self) -> str:
        return self._title

class Thing(IInventory):
    def __init__(self, number: int, title: str = "NoTitle"):
        if number < 0: raise ValueError("number must be >= 0")
        self._number = number
        self._title = title

    @property
    def number(self) -> int:
        return self._number
    @number.setter
    def number(self, value: int) -> None:
        if value < 0: raise ValueError("number must be >= 0")
        self._number = value

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def title(self):
        return self._title