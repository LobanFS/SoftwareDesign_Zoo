from typing import List, Dict, TypeVar, Generic
from src.abstract_types.global_interfaces import IInventory

T = TypeVar("T", bound = IInventory)
class GenericRepository (Generic[T]):
    def __init__(self):
        self._repository: Dict[int, T] = {}
    def add(self, item: T) -> None:
        if item.number in self._repository:
            raise ValueError(f"Инв. номер {item.number} уже используется")
        self._repository[getattr(item, "number", 0)] = item

    def get(self, number: int) -> T:
        return self._repository[number]

    def remove(self, number: int) -> bool:
        return self._repository.pop(number, None) is not None

    def all(self) -> List[T]:
        return list(self._repository.values())