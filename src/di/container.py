from src.entities.animals.herbos import Rabbit, Monkey
from src.entities.animals.predators import Wolf, Tiger
from src.entities.things.things import Computer
from src.infrastructure.factories.animal_factory import AnimalFactory
from src.services.zoo import Zoo
from src.services.vet_clinic import VetClinic
from src.infrastructure.animal_repository import AnimalRepository
from src.infrastructure.inventory_repository import InventoryRepository

class Container:
    def __init__(self):
        self.vet = VetClinic()
        self.animal_repo = AnimalRepository()
        self.inventory_repository = InventoryRepository()
        self.zoo = Zoo(self.animal_repo, self.inventory_repository)
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
        self.animal_factory = AnimalFactory(animal_cls_dict)
        self.inventory_factory = AnimalFactory(things_cls_dict)
