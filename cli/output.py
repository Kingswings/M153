# output.py
from pprint import pprint

class UserOutputHandler:

    @staticmethod
    def print_message(message):
        pprint(message)

    @staticmethod
    def print_table(table_data):
        for row in table_data:
            pprint(row)

    @staticmethod
    def print_error(error_message):
        pprint(error_message)

    @staticmethod
    def print_success(success_message):
        pprint(success_message)
