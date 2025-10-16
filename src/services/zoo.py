from src.infrastructure.repositories.generic_repository import GenericRepository, AnimalRepository, InventoryRepository
from src.abstract_types.object_types import Animal
class Zoo:
    def __init__(self, animal_repository: AnimalRepository, inventory_repository: InventoryRepository):
        self.animal_repository = animal_repository
        self.inventory_repository = inventory_repository

    def add(self, item):
        if isinstance(item, Animal):
            self.animal_repository.add(item)
        self.inventory_repository.add(item)
    def remove(self, item):
        if isinstance(item, Animal):
            self.inventory_repository.remove(item)
        self.animal_repository.remove(item)

