from src.abstract_types.global_interfaces import IVetClinic
from src.infrastructure.repositories.animal_repository import AnimalRepository
from src.infrastructure.repositories.inventory_repository import InventoryRepository
from src.abstract_types.object_types import Animal, Thing
from typing import List, Tuple

from src.services.contact_policy import IContactPolicy


class Zoo:
    def __init__(
            self,
            animal_repository: AnimalRepository,
            inventory_repository: InventoryRepository,
            vet: IVetClinic,
            contact_policy: IContactPolicy
    ):
        self._animals = animal_repository
        self._inventory = inventory_repository
        self._vet = vet
        self._contact_policy = contact_policy

    def accept_animal(self, animal: Animal) -> bool:
        if self._vet.approve(animal):
            self._animals.add(animal)
            self._inventory.add(animal)
            return True
        return False

    def add_item(self, item: Thing | Animal) -> None:
        self._inventory.add(item)

    def total_food_per_day(self) -> int:
        return sum(x.food for x in self._animals.all())

    def contact_zoo_animals(self) -> List[Animal]:
        return [x for x in self._animals.all() if self._contact_policy.can_contact(x)]

    def all_animals(self) -> list[Animal]:
        return self._animals.all()

    def inventory_list(self) -> list[Tuple[str, int]]:
        return [((getattr(x, "title", "NoTitle")), x.number) for x in self._inventory.all()]



