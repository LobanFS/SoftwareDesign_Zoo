from src.abstract_types.global_interfaces import IVetClinic, IInventory
from src.infrastructure.repositories.animal_repository import AnimalRepository
from src.infrastructure.repositories.inventory_repository import InventoryRepository
from src.abstract_types.object_types import Animal, Thing
from src.abstract_types.animal_types import Herbo
from typing import List, Tuple
class Zoo:
    def __init__(self, animal_repository: AnimalRepository, inventory_repository: InventoryRepository):
        self._animals = animal_repository
        self._inventory = inventory_repository

    def accept_animal(self, animal: Animal, vet: IVetClinic) -> bool:
        if vet.approve(animal):
            self._animals.add(animal)
            self._inventory.add(animal)
            return True
        return False

    def add_item(self, item: Thing | Animal) -> None:
        self._inventory.add(item)

    def total_food_per_day(self) -> int:
        return sum(x.food for x in self._animals.all())

    def contact_zoo_animals(self) -> list[Animal]:
        res = []
        for animal in self._animals.all():
            if isinstance(animal, Herbo) and animal.kindness_power > 5:
                res.append(animal)
        return res

    def all_animals(self) -> list[Animal]:
        return self._animals.all()

    def inventory_list(self) -> list[Tuple[str, int]]:
        return [((x.title if hasattr(x, "title") else x.name), x.number) for  x in self._inventory.all()]



