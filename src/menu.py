class Menu:

    def show(self) -> None:
        print("1. szyfruj rot13")
        print("2. deszyfruj rot13")
        print("3. szyfruj rot47")
        print("4. deszyfruj rot47")
        print("5. pokaz buffer")
        print("6. wczytaj plik")
        print("7. zapisz do pliku")
        print("8. wyjscie")

    def get_choice(self) -> str:
        self.show()
        choice = input("Dokonaj wyboru: ")
        return choice