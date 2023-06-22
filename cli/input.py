# input.py

class UserInputHandler:

    @staticmethod
    def get_input(prompt):
        return input(prompt)

    def get_integer_input(self, prompt):
        while True:
            value = self.get_input(prompt)
            if value.isdigit():
                return int(value)
            else:
                print("Ungültige Eingabe, bitte geben Sie eine Zahl ein.")

    def get_non_empty_input(self, prompt):
        while True:
            value = self.get_input(prompt)
            if value:
                return value
            else:
                print("Ungültige Eingabe, bitte geben Sie einen Wert ein.")

    def get_menu_choice(self):
        print("1. Buch anlegen")
        print("2. Buch löschen")
        print("3. Buch bearbeiten")
        print("4. Buch suchen")
        print("5. Autor anlegen")
        print("6. Autor löschen")
        print("7. Verlag anlegen")
        print("8. Verlag löschen")
        print("9. Menüeintrag anlegen")
        print("10. Menüeintrag löschen")
        print("11. Reservierung anlegen")
        print("12. Reservierung löschen")
        # ...weitere Optionen...
        return self.get_integer_input("Wählen Sie eine Option aus: ")

    def get_book_data(self):
        nummer = self.get_integer_input("Geben Sie die Buchnummer ein: ")
        title = self.get_non_empty_input("Geben Sie Ttel ein: ")
        return {"nummer": nummer, "titel": title}

    def get_autor_data(self):
        name = self.get_non_empty_input("Geben Sie den Namen des Autors ein: ")
        kontakt = self.get_non_empty_input("Geben Sie die Kontaktinformationen des Autors ein: ")
        return {"name": name, "kontakt": kontakt}

    def get_distributioner_data(self):
        name = self.get_non_empty_input("Geben Sie den Namen des Mitarbeiters ein: ")
        position = self.get_non_empty_input("Geben Sie die Position des Mitarbeiters ein: ")
        salary = self.get_integer_input("Geben Sie das Gehalt des Mitarbeiters ein: ")
        return {"name": name, "stellung": position, "gehalt": salary}

    def get_menu_data(self):
        name = self.get_non_empty_input("Geben Sie den Namen des Menüeintrags ein: ")
        preis = self.get_integer_input("Geben Sie den Preis des Menüeintrags ein: ")
        return {"name": name, "preis": preis}

    def get_reservation_data(self):
        autor_id = self.get_integer_input("Geben Sie die Autor-ID für die Reservierung ein: ")
        buch_id = self.get_integer_input("Geben Sie die Buch-ID für die Reservierung ein: ")
        datum = self.get_non_empty_input("Geben Sie das Datum der Reservierung ein (Format: JJJJ-MM-TT): ")
        return {"autor_id": autor_id, "buch_id": buch_id, "datum": datum}

