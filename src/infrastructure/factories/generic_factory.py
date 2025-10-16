from typing import TypeVar, Generic, Tuple
from src.abstract_types.global_interfaces import IFactory

T = TypeVar("T")

class GenericFactory(IFactory, Generic[T]):
    def __init__(self, cls_dict: dict[str, type[T]]):
        self._registry = {k.lower(): v for k, v in cls_dict.items()}

    def register(self, kind: str, cls: type[T]) -> None:
        self._registry[kind.lower()] = cls

    def create(self, kind: str, **kwargs) -> T:
        cls = self._registry.get(kind.lower())
        if not cls:
            raise KeyError(f"Неизвестный тип: {kind}")
        return cls(**kwargs)

    def kinds(self) -> Tuple[str, ...]:
        return tuple(sorted(self._registry.keys()))

    @property
    def registry(self):
        return self._registry
