from src.abstract_types.global_interfaces import IFactory

class AnimalFactory(IFactory):
    def __init__(self, cls_dict: dict[str, type]):
        self._registry = {k.lower(): v for k, v in cls_dict.items()}

    def register(self, kind: str, cls: type) -> None:
        self._registry[kind.lower()] = cls

    def create(self, kind: str, **kwargs):
        cls = self._registry.get(kind.lower())
        if not cls:
            raise KeyError(f"Неизвестный вид животного: {kind}")
        return cls(**kwargs)