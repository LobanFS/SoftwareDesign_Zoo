import types
import pytest
from src.services.zoo import Zoo
from src.services.contact_policy import HerbosPolicy
from src.infrastructure.factories.animal_factory import AnimalFactory
from src.infrastructure.factories.thing_factory import ThingFactory
from src.infrastructure.repositories.animal_repository import AnimalRepository
from src.infrastructure.repositories.inventory_repository import InventoryRepository
from src.abstract_types.animal_types import Herbo
from src.abstract_types.object_types import Thing
from src.services.operations import Operations
from src.services.vet_clinic import VetClinic

class Rabbit(Herbo): pass
class Table(Thing): pass

def mk_ops(approve=True):
    rnd = types.SimpleNamespace(random=(lambda: 0.99 if approve else 0.0))
    vet = VetClinic(denial_probability=0.0 if approve else 1.0, rnd=rnd)
    zoo = Zoo(AnimalRepository(), InventoryRepository(), vet, HerbosPolicy())
    animal_factory = AnimalFactory({"rabbit": Rabbit})
    thing_factory = ThingFactory({"table": Table})
    extra = {Herbo: ["kindness"]}
    return Operations(zoo, animal_factory, thing_factory, extra)

def test_operations_lists_and_extras():
    ops = mk_ops()
    assert "rabbit" in ops.get_animal_kinds()
    assert "table" in ops.get_item_kinds()
    assert ops.get_extra_fields_for_kind("rabbit") == ["kindness"]
    assert ops.get_extra_fields_for_kind("unknown") == []

def test_operations_add_item_and_inventory_list():
    ops = mk_ops()
    ops.add_item("table", number=100, title="T1")
    inv = ops.get_inventory_list()
    assert ("T1", 100) in inv

def test_operations_add_animal_success_and_contact_list():
    ops = mk_ops(approve=True)
    ok = ops.add_animal("rabbit", food_amount=4, number=1, title="R1", kindness=7)
    assert ok is True
    assert ops.get_total_food() == 4
    contact = ops.get_contact_zoo_animals()
    assert any(getattr(a, "title", "") == "R1" for a in contact)

def test_operations_add_animal_vet_denies():
    ops = mk_ops(approve=False)
    ok = ops.add_animal("rabbit", food_amount=4, number=1, title="R1", kindness=7)
    assert ok is False
    assert ops.get_total_food() == 0

def test_operations_add_animal_unknown_kind():
    ops = mk_ops()
    with pytest.raises(KeyError):
        ops.add_animal("unknown", food_amount=1, number=1)

def test_operations_add_item_unknown_kind():
    ops = mk_ops()
    with pytest.raises(KeyError):
        ops.add_item("unknown", number=1)
