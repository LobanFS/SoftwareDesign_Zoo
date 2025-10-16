from dataclasses import dataclass
from typing import Callable, Optional

@dataclass(frozen=True)
class Command:
    key: str
    label: str
    handler: Callable[[], Optional[bool]]
    pause_after: bool = True

class ConsoleUI:
    def __init__(self, operations, input_func=input, output_func=print):
        self.ops = operations
        self._in = input_func
        self._out = output_func

        self._commands: dict[str, Command] = {}
        self._register(
            Command("1", "Принять животное", self._add_animal),
            Command("2", "Принять вещь", self._add_item),
            Command("3", "Список всех животных", self._list_animals),
            Command("4", "Список для контактного зоопарка", self._list_contact_animals),
            Command("5", "Всего корма в день (кг)", self._show_food_sum),
            Command("6", "Инвентаризация (название, номер)", self._list_inventory),
            Command("0", "Выход", self._exit, pause_after=False),
        )

    def run(self):
        running = True
        while running:
            self._print_menu()
            cmd = self._ask_str("Выбери пункт: ")

            command = self._commands.get(cmd)
            if not command:
                self._out("Неизвестная команда.")
                self._pause()
                continue

            try:
                cont = command.handler()
            except (KeyboardInterrupt, EOFError):
                self._out("\nВыход.")
                return
            except Exception as e:
                self._out(f"Ошибка: {e}")
                cont = True

            if command.pause_after and cont is not False:
                self._pause()
            if cont is False:
                running = False

    def _register(self, *cmds: Command):
        for c in cmds:
            self._commands[c.key] = c

    def _print_menu(self):
        self._out("\n--- Зоопарк ---")
        for key in sorted(self._commands.keys(), key=lambda k: (k != "0", k)):
            c = self._commands[key]
            self._out(f"{c.key}) {c.label}")

    def _pause(self, msg: str = "\nНажми Enter, чтобы продолжить..."):
        self._in(msg)

    def _ask_str(self, prompt: str, *, default: Optional[str] = None) -> str:
        s = self._in(prompt).strip()
        if s:
            return s
        return default if default is not None else ""

    def _ask_int(self, prompt: str, *, min_value: int | None = None, max_value: int | None = None) -> int:
        while True:
            raw = self._in(prompt).strip()
            try:
                val = int(raw)
            except ValueError:
                self._out("Нужно целое число. Попробуй снова.")
                continue
            if min_value is not None and val < min_value:
                self._out(f"Число должно быть ≥ {min_value}.")
                continue
            if max_value is not None and val > max_value:
                self._out(f"Число должно быть ≤ {max_value}.")
                continue
            return val

    def _ask_choice(self, prompt: str, options: tuple[str, ...]) -> str:
        shown = "/".join(options)
        while True:
            val = self._in(f"{prompt} ({shown}): ").strip().lower()
            if val in options:
                return val
            self._out(f"Неизвестный вариант. Введи один из: {shown}")

    def _add_animal(self) -> bool:
        kinds = self.ops.get_animal_kinds()
        if not kinds:
            self._out("Нет зарегистрированных видов животных.")
            return True

        kind = self._ask_choice("Вид", kinds)
        number = self._ask_int("Инв. номер: ", min_value=0)
        title = self._ask_str("Кличка: ") or "NoTitle"
        food = self._ask_int("Кг корма в день: ", min_value=0)

        extra_fields = self.ops.get_extra_fields_for_kind(kind)
        extra: dict[str, object] = {}
        for field in extra_fields:
            if field == "kindness":
                extra[field] = self._ask_int("Доброта (0...10): ", min_value=0, max_value=10)
            else:
                extra[field] = self._ask_str(f"{field.capitalize()}: ")
        try:
            ok = self.ops.add_animal(kind, food_amount=food, number=number, title=title, **extra)
        except KeyError as e:
            self._out(str(e))
            return True
        except ValueError as e:
            self._out(f"Ошибка данных: {e}")
            return True
        self._out("Приняли!" if ok else "Отклонено ветеринаром :(")
        return True

    def _add_item(self) -> bool:
        kinds = self.ops.get_item_kinds()
        if not kinds:
            self._out("Нет зарегистрированных типов вещей.")
            return True
        kind = self._ask_choice("Тип вещи", kinds)
        number = self._ask_int("Номер: ", min_value=0)
        title = self._ask_str("Название: ") or "NoTitle"
        try:
            self.ops.add_item(kind, number=number, title=title)
        except KeyError as e:
            self._out(str(e))
            return True
        except ValueError as e:
            self._out(f"Ошибка данных: {e}")
            return True
        self._out("Добавлено.")
        return True

    def _list_animals(self) -> bool:
        animals = self.ops.get_all_animals()
        if not animals:
            self._out("Животных пока нет.")
            return True
        for a in animals:
            self._out(f"{a.name} #{a.number} '{a.title}', food/day={a.food}")
        return True

    def _list_contact_animals(self) -> bool:
        lst = self.ops.get_contact_zoo_animals()
        if not lst:
            self._out("Пока пусто.")
            return True
        for a in lst:
            self._out(f"{a.name} #{a.number} '{a.title}' (kindness={getattr(a, 'kindness', '-')})")
        return True

    def _show_food_sum(self) -> bool:
        total = self.ops.get_total_food()
        self._out("Всего корма в день:", total, "кг")
        return True

    def _list_inventory(self) -> bool:
        items = self.ops.get_inventory_list()
        if not items:
            self._out("Инвентаризационный список пуст.")
            return True
        for title, num in items:
            self._out(f"{title} — #{num}")
        return True

    def _exit(self) -> bool:
        self._out("Пока!")
        return False
