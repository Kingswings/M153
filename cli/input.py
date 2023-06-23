# input.py
from pprint import pprint

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
                pprint("Invalid input, please enter a number.")

    def get_non_empty_input(self, prompt):
        while True:
            value = self.get_input(prompt)
            if value:
                return value
            else:
                pprint("Invalid input, please enter a value.")

    def get_menu_choice(self):
        pprint("1. Create book")
        pprint("2. Delete book")
        pprint("3. Edit book")
        pprint("4. Filter books")
        pprint("5. Search book by number")
        pprint("6. Show all books")
        pprint("7. Create author")
        pprint("8. Delete author")
        pprint("9. Create publisher")
        pprint("10. Delete publisher")
        pprint("11. Create menu item")
        pprint("12. Delete menu item")
        pprint("13. Create reservation")
        pprint("14. Delete reservation")
        # ...weitere Optionen...
        return self.get_integer_input("Select an option: ")

    def get_book_data(self):
        nummer = self.get_integer_input("Enter the book number: ")
        title = self.get_non_empty_input("Enter the title: ")
        return {"nummer": nummer, "titel": title}

    def get_autor_data(self):
        name = self.get_non_empty_input("Enter the author's name: ")
        kontakt = self.get_non_empty_input("Enter the author's contact information: ")
        return {"name": name, "kontakt": kontakt}

    def get_distributioner_data(self):
        name = self.get_non_empty_input("Enter the employee's name: ")
        position = self.get_non_empty_input("Enter the employee's position: ")
        salary = self.get_integer_input("Enter the employee's salary: ")
        return {"name": name, "stellung": position, "gehalt": salary}

    def get_menu_data(self):
        name = self.get_non_empty_input("Enter the menu item name: ")
        preis = self.get_integer_input("Enter the menu item price: ")
        return {"name": name, "preis": preis}

    def get_reservation_data(self):
        autor_id = self.get_integer_input("Enter the author ID for the reservation: ")
        buch_id = self.get_integer_input("Enter the book ID for the reservation: ")
        datum = self.get_non_empty_input("Enter the reservation date (Format: YYYY-MM-DD): ")
        return {"autor_id": autor_id, "buch_id": buch_id, "datum": datum}

