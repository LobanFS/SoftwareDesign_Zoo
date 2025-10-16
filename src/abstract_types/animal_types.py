from abc import ABC
from .object_types import Animal

class Herbo(ABC, Animal):
    def __init__(self, food_amount, number, kindness):
        super().__init__(food_amount = food_amount, number = number)
        self._kindness = max(0, min(10, kindness))

    @property
    def kindness_power(self) -> int:
        return self._kindness
    @kindness_power.setter
    def kindness_power(self, value: int) -> None:
        self._kindness = max(0, min(10, value))

class Predator(ABC, Animal):
    pass
