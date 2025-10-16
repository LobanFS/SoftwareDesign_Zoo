import random
class VetClinic:
    def __init__(self, denial_probability = 0.2):
        self.denial_probability = denial_probability
    def is_animal_healthy(self) -> bool:
        medical_expertise = random.randint(0, 100) % 100
        if medical_expertise < self.denial_probability * 100:
            return False
        return True


