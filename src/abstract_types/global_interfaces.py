from abc import ABC, abstractmethod

class IAlive(ABC):
    @property
    @abstractmethod
    def food(self):
        pass
class IInventory(ABC):
    @property
    @abstractmethod
    def number(self):
        pass