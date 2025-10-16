from src.abstract_types.global_interfaces import IFactory
from .generic_factory import GenericFactory
from src.abstract_types.object_types import Animal

class AnimalFactory(GenericFactory[Animal]):
    pass