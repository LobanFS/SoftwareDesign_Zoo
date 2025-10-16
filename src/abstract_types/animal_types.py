from abc import ABC
from .object_types import Animal

class Herbo(ABC, Animal):
    def __init__(self, food_amount, animal_id, kindness):
        super().__init__(food_amount, animal_id)
        self._kindness = kindness

    @property
    def Kindness_power(self) -> int:
        return self._kindness
    @Kindness_power.setter
    def Kindness_power(self, value):
        self._kindness = value

class Predator(ABC, Animal):
    pass
