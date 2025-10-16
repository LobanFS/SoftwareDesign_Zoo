from __future__ import annotations
from src.infrastructure.factories.animal_factory import AnimalFactory
from src.infrastructure.factories.thing_factory import ThingFactory
from src.services.zoo import Zoo
from src.abstract_types.object_types import Animal, Thing
from src.abstract_types.global_interfaces import IVetClinic

class Operations:
    def __init__(self, zoo: Zoo, animal_factory: AnimalFactory, item_factory: ThingFactory, vet: IVetClinic):
        self.zoo = zoo
        self.animal_factory = animal_factory
        self.item_factory = item_factory
        self.vet = vet

    def add_animal(self, kind: str, *, food_amount: int, number: int, title:str = "NoTitle", **kwargs) -> bool:
        animal: Animal = self.animal_factory.create(
            kind,
            food_amount=food_amount,
            number=number,
            title = title,
            **kwargs
        )
        return self.zoo.accept_animal(animal, self.vet)

    def add_item(self, kind: str, *, number: int, title: str | None = None, **kwargs) -> None:
        item = self.item_factory.create(kind, number=number, title=title, **kwargs)
        self.zoo.add_item(item)

    def get_total_food(self) -> int:
        return self.zoo.total_food_per_day()

    def get_contact_zoo_animals(self):
        return list(self.zoo.contact_zoo_animals())

    def get_inventory_list(self):
        return self.zoo.inventory_list()

    def get_all_animals(self):
        return list(self.zoo.all_animals())
