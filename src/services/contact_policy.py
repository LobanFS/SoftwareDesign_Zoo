# services/contact_policy.py
from abc import ABC, abstractmethod
from src.abstract_types.object_types import Animal
from src.abstract_types.animal_types import Herbo

class IContactPolicy(ABC):
    @abstractmethod
    def can_contact(self, animal: Animal) -> bool: ...

class HerbosPolicy(IContactPolicy):
    def __init__(self, threshold: int = 5):
        self.threshold = threshold
    def can_contact(self, animal: Animal) -> bool:
        return isinstance(animal, Herbo) and getattr(animal, "kindness", 0) > self.threshold
