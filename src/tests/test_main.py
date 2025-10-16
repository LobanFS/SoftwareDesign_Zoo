from src import main as main_mod

def test_main_calls_ui_run(monkeypatch):
    run_called = {"flag": False}

    class DummyUI:
        def __init__(self, *args, **kwargs):
            pass
        @staticmethod
        def run():
            run_called["flag"] = True

    class DummyContainer:
        def __init__(self):
            self.ops = object()

    monkeypatch.setattr(main_mod, "ConsoleUI", DummyUI)
    monkeypatch.setattr(main_mod, "Container", DummyContainer)

    main_mod.main()
    assert run_called["flag"] is True
