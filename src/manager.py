from facade import Facade
from menu import Menu

class Manager:
    def __init__(self):
        self.facade = Facade()
        self.menu = Menu()

    def run(self, command):
        match command:
            case "1":
                text = input("Podaj tekst do zakodowania w ROT13: ")
                self.facade.encrypt_rot13(text)
            case "2":
                text = input("Podaj tekst do odkodowania w ROT13: ")
                self.facade.decrypt_rot13(text)
            case "3":
                text = input("Podaj tekst do zakodowania w ROT47: ")
                self.facade.encrypt_rot47(text)
            case "4":
                text = input("Podaj tekst do odkodowania w ROT47: ")
                self.facade.decrypt_rot47(text)
            case "5":
                print(self.facade.get_buffer())
            case "6":
                text = input("Podaj nazwę pliku: ")
                if not text.endswith(".json"):
                    text += ".json"
                self.facade.load_from_file(text)
            case "7":
                text = input("Podaj nazwe pliku: ")
                if not text.endswith(".json"):
                    text += ".json"
                self.facade.save_to_file(text)
            case "8":
                exit()
            case _:
                print("błędny wybór")

    def start(self):
        while True:
            choice = self.menu.get_choice()
            self.run(choice)