from __future__ import annotations
from src.entities.animals.herbos import Rabbit, Monkey
from src.entities.animals.predators import Wolf, Tiger
from src.entities.things.things import Table, Computer
from src.infrastructure.factories.animal_factory import AnimalFactory
from src.infrastructure.factories.thing_factory import ThingFactory
from src.infrastructure.repositories.inventory_repository import InventoryRepository
from src.infrastructure.repositories.animal_repository import AnimalRepository
from src.services.zoo import Zoo
from src.services.vet_clinic import VetClinic
from src.services.operations import Operations
from src.services.contact_policy import HerbosPolicy
from src.abstract_types.animal_types import Herbo, Predator

class Container:
    def __init__(self):
        vet = VetClinic()
        animal_repository = AnimalRepository()
        inventory_repository = InventoryRepository()
        contact_policy = HerbosPolicy(threshold = 5)
        zoo = Zoo(animal_repository, inventory_repository, vet, contact_policy)

        animal_cls_dict = {
            "monkey" : Monkey,
            "rabbit" : Rabbit,
            "tiger" : Tiger,
            "wolf" : Wolf
        }

        things_cls_dict = {
            "table" : Table,
            "computer" : Computer
        }

        animal_extra_fields_by_class = {
            Herbo: ["kindness"],
            Predator: []
        }

        animal_factory = AnimalFactory(animal_cls_dict)
        thing_factory = ThingFactory(things_cls_dict)

        self.ops = Operations(zoo, animal_factory, thing_factory, animal_extra_fields_by_class)
