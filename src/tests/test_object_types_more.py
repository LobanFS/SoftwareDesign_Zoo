import pytest
from src.abstract_types.object_types import Animal, Thing

def test_animal_number_setter_ok_and_negative():
    a = Animal(food_amount=1, number=1, title="A")
    a.number = 5
    assert a.number == 5
    with pytest.raises(ValueError):
        a.number = -1

def test_animal_food_setter_ok_and_negative():
    a = Animal(food_amount=1, number=1, title="A")
    a.food = 0
    assert a.food == 0
    a.food = 7
    assert a.food == 7
    with pytest.raises(ValueError):
        a.food = -3

def test_thing_number_setter_ok_and_negative():
    t = Thing(1, "T")
    t.number = 10
    assert t.number == 10
    with pytest.raises(ValueError):
        t.number = -2

def test_animal_defaults_and_zero_values():
    a = Animal(food_amount=0, number=0)
    assert a.food == 0
    assert a.number == 0
    assert a.title == "NoTitle"

def test_thing_defaults_and_zero_values():
    t = Thing(0)
    assert t.number == 0
    assert t.title == "NoTitle"

def test_animal_name_is_subclass_name():
    class Lynx(Animal):
        pass
    x = Lynx(food_amount=1, number=1, title="L")
    assert x.name == "Lynx"

def test_thing_name_is_subclass_name():
    class Chair(Thing):
        pass
    c = Chair(2, "C")
    assert c.name == "Chair"
