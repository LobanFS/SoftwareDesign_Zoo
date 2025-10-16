from __future__ import annotations
from src.infrastructure.factories.animal_factory import AnimalFactory
from src.infrastructure.factories.thing_factory import ThingFactory
from src.services.zoo import Zoo
from src.abstract_types.object_types import Animal

class Operations:
    def __init__(self, zoo: Zoo, animal_factory: AnimalFactory, item_factory: ThingFactory, extra_fields_by_class):
        self.zoo = zoo
        self.animal_factory = animal_factory
        self.item_factory = item_factory
        self._extra_fields_by_class = extra_fields_by_class

    def get_animal_kinds(self) -> tuple[str, ...]:
        return self.animal_factory.kinds()

    def get_item_kinds(self) -> tuple[str, ...]:
        return self.item_factory.kinds()

    def add_animal(self, kind: str, *, food_amount: int, number: int, title:str = "NoTitle", **kwargs) -> bool:
        animal: Animal = self.animal_factory.create(
            kind,
            food_amount = food_amount,
            number = number,
            title = title,
            **kwargs
        )
        return self.zoo.accept_animal(animal)

    def add_item(self, kind: str, *, number: int, title: str = "NoTitle", **kwargs) -> None:
        item = self.item_factory.create(kind, number = number, title = title, **kwargs)
        self.zoo.add_item(item)

    def get_total_food(self) -> int:
        return self.zoo.total_food_per_day()

    def get_contact_zoo_animals(self):
        return list(self.zoo.contact_zoo_animals())

    def get_inventory_list(self):
        return self.zoo.inventory_list()

    def get_all_animals(self):
        return list(self.zoo.all_animals())

    def get_extra_fields_for_kind(self, kind: str) -> list[str]:
        cls = self.animal_factory.registry.get(kind.lower())
        if not cls:
            return []
        for base_cls, fields in self._extra_fields_by_class.items():
            if issubclass(cls, base_cls):
                return fields
        return []
