from src.abstract_types.global_interfaces import IFactory

class AnimalFactory(IFactory):
    def __init__(self, cls_dict):
        self._registry = cls_dict
    def register(self, kind: str, cls):
        self._registry[kind.lower()] = cls
    def create(self, kind: str, **kwargs):
        cls = self._registry.get(kind.lower())
        return cls(**kwargs)