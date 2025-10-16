import pytest
from src.abstract_types.object_types import Animal, Thing
from src.abstract_types.animal_types import Herbo

def test_animal_ok():
    a = Animal(food_amount=3, number=1, title="Bob")
    assert a.food == 3 and a.number == 1 and a.title == "Bob"

@pytest.mark.parametrize("field", ["food_amount", "number"])
def test_animal_negative_raises(field):
    kwargs = dict(food_amount=1, number=1)
    kwargs[field] = -1
    with pytest.raises(ValueError):
        Animal(**kwargs)

def test_thing_negative_number():
    with pytest.raises(ValueError):
        Thing(number=-5)

def test_herbo_kindness_clamped():
    h = Herbo(food_amount=1, number=1, title="h", kindness=999)
    assert h.kindness == 10
    h.kindness = -7
    assert h.kindness == 0
