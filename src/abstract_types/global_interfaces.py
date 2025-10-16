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
class IRepository(ABC):
    @abstractmethod
    def add(self, **kwargs):
        pass
    @abstractmethod
    def remove(self, number:int):
        pass
    @abstractmethod
    def get(self, number:int):
        pass
class IFactory(ABC):
    @abstractmethod
    def create(self, *args):
        pass
