from src.ui.console_ui import ConsoleUI

class FakeOps:
    def __init__(self):
        self.animals = []
        self.items = []
        self.add_animal_calls = []
        self.add_item_calls = []
    @staticmethod
    def get_animal_kinds(): return "rabbit", "tiger"
    @staticmethod
    def get_item_kinds(): return "table", "computer"
    def get_all_animals(self): return list(self.animals)
    def get_contact_zoo_animals(self): return [a for a in self.animals if getattr(a, "kindness", 0) > 5]
    def get_total_food(self): return sum(getattr(a, "food", 0) for a in self.animals)
    def get_inventory_list(self):
        return [(x.get("title", "NoTitle"), x["number"]) for x in self.items]

    @staticmethod
    def get_extra_fields_for_kind(kind: str):
        return ["kindness"] if kind == "rabbit" else []

    def add_animal(self, kind, *, food_amount, number, title="NoTitle", **kwargs) -> bool:
        self.add_animal_calls.append((kind, food_amount, number, title, kwargs))
        animal = type("A", (), {})()
        animal.name = kind.capitalize()
        animal.number = number
        animal.title = title
        animal.food = food_amount
        for k, v in kwargs.items(): setattr(animal, k, v)
        self.animals.append(animal)
        return True

    def add_item(self, kind, *, number, title="NoTitle", **kwargs):
        self.add_item_calls.append((kind, number, title, kwargs))
        self.items.append({"kind": kind, "number": number, "title": title})

def test_console_ui_basic_flow():
    ops = FakeOps()

    inputs = iter([
        "3", "",
        "2", "table", "100", "T1", "",
        "6", "",
        "1", "rabbit", "1", "Bugs", "5", "7", "",
        "5", "",
        "4", "",
        "0"
    ])

    out = []
    ui = ConsoleUI(ops, input_func=lambda p="": next(inputs), output_func=lambda *a: out.append(" ".join(map(str, a))))
    ui.run()
    assert ("T1", 100) in ops.get_inventory_list()
    assert len(ops.get_all_animals()) == 1
    assert len(ops.get_contact_zoo_animals()) == 1
    assert any("Инвентаризационный список" in line or "— #100" in line or "Добавлено." in line for line in out)

def test_console_ui_input_validation():
    ops = FakeOps()
    inputs = iter([
        "9", "",
        "2", "computer", "abc", "200", "PC", "",
        "0"
    ])
    out = []
    ui = ConsoleUI(ops, input_func=lambda p="": next(inputs), output_func=lambda *a: out.append(" ".join(map(str, a))))
    ui.run()
    assert any("Нужно целое число" in line for line in out)
    assert ("PC", 200) in ops.get_inventory_list()
