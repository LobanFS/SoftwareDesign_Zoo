from src.services.contact_policy import HerbosPolicy
from src.abstract_types.animal_types import Herbo

def test_herbos_policy_threshold():
    p = HerbosPolicy(threshold=5)
    h1 = Herbo(food_amount=1, number=1, title="h1", kindness=5)
    h2 = Herbo(food_amount=1, number=2, title="h2", kindness=6)
    assert p.can_contact(h1) is False
    assert p.can_contact(h2) is True
