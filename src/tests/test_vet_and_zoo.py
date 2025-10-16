import types
import pytest
from src.services.vet_clinic import VetClinic
from src.services.zoo import Zoo
from src.infrastructure.repositories.animal_repository import AnimalRepository
from src.infrastructure.repositories.inventory_repository import InventoryRepository
from src.services.contact_policy import HerbosPolicy
from src.abstract_types.animal_types import Herbo

def mk_zoo(denial_p, rnd=None):
    vet = VetClinic(denial_probability=denial_p, rnd=rnd)
    return Zoo(AnimalRepository(), InventoryRepository(), vet, HerbosPolicy())

def test_zoo_accepts_when_vet_approves():
    rnd = types.SimpleNamespace(random=lambda: 0.99)
    zoo = mk_zoo(denial_p=0.2, rnd=rnd)
    h = Herbo(food_amount=3, number=1, title="h", kindness=7)
    assert zoo.accept_animal(h) is True
    assert zoo.total_food_per_day() == 3
    assert len(zoo.inventory_list()) == 1

def test_zoo_rejects_when_vet_denies():
    rnd = types.SimpleNamespace(random=lambda: 0.0)
    zoo = mk_zoo(denial_p=1.0, rnd=rnd)
    h = Herbo(food_amount=3, number=1, title="h", kindness=7)
    assert zoo.accept_animal(h) is False
    assert len(zoo.all_animals()) == 0
    assert len(zoo.inventory_list()) == 0

def test_zoo_transaction_rollback_on_inventory_error(monkeypatch):
    rnd = types.SimpleNamespace(random=lambda: 0.99)
    zoo = mk_zoo(denial_p=0.0, rnd=rnd)
    h1 = Herbo(food_amount=1, number=1, title="h1", kindness=7)
    h2 = Herbo(food_amount=2, number=1, title="h2", kindness=8)

    assert zoo.accept_animal(h1) is True

    def boom(): raise ValueError("dup")
    monkeypatch.setattr(type(zoo._inventory), "add", lambda *_args, **_kw: boom())

    with pytest.raises(ValueError):
        zoo.accept_animal(h2)
    assert len(zoo.all_animals()) == 1
