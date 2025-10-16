from abc import ABC, abstractmethod

class IAlive(ABC):
    @property
    @abstractmethod
    def Food(self):
        pass
class IInventory(ABC):
    @property
    @abstractmethod
    def Number(self):
        pass