from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
# Маркер живых сущностей
class IAlive(ABC):
    @property
    @abstractmethod
    def food(self) -> int: ...

# Можно инвенторизовать
class IInventory(ABC):
    @property
    @abstractmethod
    def number(self) -> int: ...

# Хранить должны только инвентаризируемые классы.
T = TypeVar("T", bound=IInventory)
# Хранилище
class IRepository(ABC, Generic[T]):
    @abstractmethod
    def add(self, item: T) -> None: ...
    @abstractmethod
    def remove(self, number:int) -> bool: ...
    @abstractmethod
    def get(self, number:int) -> T: ...
    @abstractmethod
    def all(self) -> List[T]: ...

# Фабрика
class IFactory(ABC):
    @abstractmethod
    def create(self, *args): ...

class IVetClinic(ABC):
    @abstractmethod
    def approve(self, animal: IAlive) -> bool: ...