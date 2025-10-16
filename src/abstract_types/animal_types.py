from abc import ABC
from .object_types import Animal

class Herbo(ABC, Animal):
    def __init__(self, food_amount, animal_id, kindness):
        super().__init__(food_amount, animal_id)
        self._kindness = kindness

    @property
    def kindness_power(self) -> int:
        return self._kindness
    @kindness_power.setter
    def kindness_power(self, value):
        self._kindness = value

class Predator(ABC, Animal):
    pass
