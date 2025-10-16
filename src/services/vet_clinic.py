import random
from src.abstract_types.global_interfaces import IVetClinic, IAlive

class VetClinic(IVetClinic):
    def __init__(self, denial_probability=0.2, rnd=None):
        self.denial_probability = denial_probability
        self._rnd = rnd or random
    def approve(self, animal: IAlive) -> bool:
        return self._rnd.random() >= self.denial_probability


