from .object_types import Animal

class Herbo(Animal):
    def __init__(self, *, food_amount, number, title, kindness):
        super().__init__(food_amount = food_amount, number = number, title = title)
        self.kindness = kindness

    @property
    def kindness(self) -> int:
        return self._kindness
    @kindness.setter
    def kindness(self, value: int) -> None:
        if value is None: value = 0
        self._kindness = max(0, min(10, int(value)))

class Predator(Animal):
    pass
