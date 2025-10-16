import pytest
from src.infrastructure.repositories.generic_repository import GenericRepository
from src.abstract_types.object_types import Thing

def test_repo_add_get_remove_all():
    repo = GenericRepository[Thing]()
    t1 = Thing(1, "A")
    t2 = Thing(2, "B")
    repo.add(t1); repo.add(t2)
    assert len(repo.all()) == 2
    assert repo.get(1).title == "A"
    assert repo.remove(1) is True
    assert repo.remove(1) is False

def test_repo_duplicate_number_raises():
    repo = GenericRepository[Thing]()
    repo.add(Thing(1, "A"))
    with pytest.raises(ValueError):
        repo.add(Thing(1, "B"))
