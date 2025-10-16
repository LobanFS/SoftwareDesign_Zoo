import random
from src.abstract_types.global_interfaces import IVetClinic, IAlive

class VetClinic(IVetClinic):
    def __init__(self, denial_probability = 0.2):
        self.denial_probability = denial_probability
    def approve(self, animal: IAlive) -> bool:
        medical_expertise = random.randint(0, 100)
        if medical_expertise < self.denial_probability * 100:
            return False
        return True


