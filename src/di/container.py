from src.entities.animals.herbos import Rabbit, Monkey
from src.entities.animals.predators import Wolf, Tiger
from src.entities.things.things import Computer
from src.infrastructure.factories.animal_factory import AnimalFactory
from src.services.zoo import Zoo
from src.services.vet_clinic import VetClinic
from src.infrastructure.repositories.inventory_repository import InventoryRepository
from src.infrastructure.repositories.animal_repository import AnimalRepository

class Container:
    def __init__(self):
        vet = VetClinic()
        animal_repository = AnimalRepository()
        inventory_repository = InventoryRepository()
        zoo = Zoo(animal_repository, inventory_repository)

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

        animal_factory = AnimalFactory(animal_cls_dict)
        inventory_factory = AnimalFactory(things_cls_dict)

        self.ops = Operations(zoo, animal_factory, inventory_factory, vet)
