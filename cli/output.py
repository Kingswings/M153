# output.py

class UserOutputHandler:

    @staticmethod
    def print_message(message):
        print(message)

    @staticmethod
    def print_table(table_data):
        for row in table_data:
            print(row)

    @staticmethod
    def print_error(error_message):
        print("Fehler: ", error_message)

    @staticmethod
    def print_success(success_message):
        print("Erfolg: ", success_message)
