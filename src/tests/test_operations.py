from src.di.container import Container

def test_operations_end_to_end_happy_path():
    c = Container()
    ops = c.ops
    kinds = ops.get_animal_kinds()
    assert "rabbit" in kinds

    # добавим вещь
    ops.add_item("table", number=100, title="T1")
    assert ("T1", 100) in ops.get_inventory_list()

    ok = ops.add_animal("rabbit", food_amount=5, number=1, title="R1", kindness=7)
    assert ok in (True, False)

    assert ops.get_extra_fields_for_kind("rabbit") == ["kindness"]
