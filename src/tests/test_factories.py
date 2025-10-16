import pytest
from src.infrastructure.factories.generic_factory import GenericFactory
from src.abstract_types.object_types import Thing

class Table(Thing): pass

def test_factory_create_and_kinds():
    f = GenericFactory[Thing]({"table": Table})
    obj = f.create("table", number=10, title="T")
    assert isinstance(obj, Table)
    assert "table" in f.kinds()

def test_factory_unknown_kind():
    f = GenericFactory[Thing]({})
    with pytest.raises(KeyError):
        f.create("unknown", number=1)
