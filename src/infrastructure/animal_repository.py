from src.abstract_types.object_types import Animal
from src.abstract_types.global_interfaces import IRepository
from typing import Dict
class AnimalRepository(IRepository):
    def __init__(self):
        self._repository: Dict[int, Animal] = {}

    def add(self, animal: Animal) -> None:
        self._repository[animal.id] = animal

    def get(self, number: int) -> Animal:
        return self._repository[number]

    def remove(self, number: int) -> None:
        return self._repository.pop(number, None) is not None