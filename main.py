from src.di.container import Container
from src.ui.console_ui import ConsoleUI

def main():
    container = Container()
    ui = ConsoleUI(container.ops)
    ui.run()

if __name__ == "__main__":
    main()