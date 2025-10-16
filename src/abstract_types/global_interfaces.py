from abc import ABC, abstractmethod
from typing import Iterable
from src.abstract_types.object_types import Animal
# Маркер живых сущностей
class IAlive(ABC):
    @property
    @abstractmethod
    def food(self) -> int:
        pass

# Можно инвенторизовать
class IInventory(ABC):
    @property
    @abstractmethod
    def number(self) -> int:
        pass

# Хранить должны только инвентаризируемые классы.
T = TypeVar("T", bound=IInventory)

# Хранилище
class IRepository(ABC, Generic[T]):
    @abstractmethod
    def add(self, **kwargs) -> None:
        pass
    @abstractmethod
    def remove(self, number:int) -> None:
        pass
    @abstractmethod
    def get(self, number:int) -> T:
        pass
    @abstractmethod
    def all(self) -> Iterable[T]:
        pass

# Фабрика
class IFactory(ABC):
    @abstractmethod
    def create(self, *args):
        pass

class IVetClinic(ABC):
    @abstractmethod
    def approve(self, animal: "Animal") -> bool:
        pass