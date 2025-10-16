from src.abstract_types.object_types import Animal
from src.abstract_types.global_interfaces import IInventory
from typing import Dict
class InventoryRepository:
    def __init__(self):
        self._repository: Dict[int, IInventory] = {}

    def add(self, item: IInventory) -> None:
        self._repository[item.number] = item

    def get(self, number: int) -> IInventory:
        return self._repository[number]

    def remove(self, number: int) -> None:
        return self._repository.pop(number, None) is not None