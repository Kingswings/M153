from cli.input import UserInputHandler
from cli.output import UserOutputHandler
from config import DB_CONFIG
from database.db import Database
from database.models import Autor, Buch, Verlag, Menue, Reservierung
from database.queries import Query
from logger import logger


def main():
    # Create instances of classes
    db = Database(DB_CONFIG)
    db.connect()
    db.create_tables()

    input_handler = UserInputHandler()
    output_handler = UserOutputHandler()

    buch_query = Query(Buch())
    autor_query = Query(Autor())
    verlag_query = Query(Verlag())
    menue_query = Query(Menue())
    reservierung_query = Query(Reservierung())

    # Main menu
    while True:
        choice = input_handler.get_menu_choice()

        # Create a switch statement for menu choices
        switch = {
            1: create_book,
            2: delete_book,
            3: update_book,
            4: search_book_by_condition,
            5: search_book_by_column_value,
            6: create_author,
            7: delete_author,
            8: create_publisher,
            9: delete_publisher,
            10: create_menu_entry,
            11: delete_menu_entry,
            12: create_reservation,
            13: delete_reservation,
        }

        # Execute the selected choice from the switch statement
        func = switch.get(choice)
        if func:
            func(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query)
        else:
            output_handler.print_error("Invalid choice, please try again.")
            logger.warning("Invalid choice, please try again.")


def create_book(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    data = input_handler.get_book_data()
    query, params = buch_query.create_insert_query(data)
    try:
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        db.connection.commit()
        output_handler.print_success("Book created successfully.")
        logger.info("Book created successfully.")
    except Exception as e:
        db.connection.rollback()
        if "unique constraint" in str(e).lower():
            output_handler.print_error("A book with this number already exists.")
            logger.error("A book with this number already exists.")
        else:
            output_handler.print_error("An error occurred.")
            logger.error("An error occurred: %s", str(e))


def delete_book(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    book_number = input_handler.get_integer_input("Enter the number of the book to delete: ")
    query, params = buch_query.create_delete_query(f"nummer = {book_number}")
    try:
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        db.connection.commit()
        if cursor.rowcount == 0:
            raise Exception("Book does not exist.")
        output_handler.print_success("Book deleted successfully.")
        logger.info("Book deleted successfully.")
    except Exception as e:
        db.connection.rollback()
        if "Book does not exist" in str(e):
            output_handler.print_error("No book exists with this number.")
            logger.error("No book exists with this number.")
        else:
            output_handler.print_error("An error occurred.")
            logger.error("An error occurred: %s", str(e))


def update_book(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    try:
        data = input_handler.get_book_data()  # Get the updated book data
        condition = "nummer = {}".format(data['nummer'])  # Assuming 'nummer' is the primary key or unique identifier
        stmt, values = buch_query.create_update_query(condition, data)
        cursor = db.connection.cursor()
        cursor.execute(stmt, values)
        db.connection.commit()
        output_handler.print_success("Book updated successfully.")
        logger.info("Book updated.")
    except Exception as e:
        db.connection.rollback()
        output_handler.print_error("An error occurred.")
        logger.error("An error occurred: %s", str(e))


def search_book_by_condition(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    data = input_handler.get_book_data()
    condition = "nummer = {}".format(data['nummer'])
    query, params = buch_query.create_select_where_query(condition)
    try: 
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()

        # Handle the output
        if len(rows) == 0:
            output_handler.print_error("No matching records found.")
        else:
            output_handler.print_success("Matching records:")
            for row in rows:
                output_handler.print_success(row)
    except Exception as e:
        db.connection.rollback()
        output_handler.print_error("An error occurred.")
        logger.error("An error occurred: %s", str(e))


def search_book_by_column_value(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    table_name = "buch"  # Replace with the appropriate table name
    column = input_handler.get_non_empty_input("Enter the column name: ")
    value = input_handler.get_non_empty_input("Enter the search value: ")
    query, params = buch_query.create_search_query(table_name, column, value)
    try:
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()

        # Handle the output
        if len(rows) == 0:
            output_handler.print_error("No matching records found.")
        else:
            output_handler.print_success("Matching records:")
            for row in rows:
                output_handler.print_success(row)
    except Exception as e:
        db.connection.rollback()
        output_handler.print_error("An error occurred.")
        logger.error("An error occurred: %s", str(e))


def create_author(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    data = input_handler.get_author_data()
    query, params = autor_query.create_insert_query(data)
    try:
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        db.connection.commit()
        output_handler.print_success("Author created successfully.")
        logger.info("Author created successfully.")
    except Exception as e:
        db.connection.rollback()
        output_handler.print_error("An error occurred.")
        logger.error("An error occurred: %s", str(e))


def delete_author(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    author_name = input_handler.get_non_empty_input("Enter the name of the author to delete: ")
    query, params = autor_query.create_delete_query(f"name = '{author_name}'")
    try:
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        db.connection.commit()
        output_handler.print_success("Author deleted successfully.")
        logger.info("Author deleted successfully.")
    except Exception as e:
        db.connection.rollback()
        output_handler.print_error("An error occurred.")
        logger.error("An error occurred: %s", str(e))


def create_publisher(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    data = input_handler.get_publisher_data()
    query, params = verlag_query.create_insert_query(data)
    try:
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        db.connection.commit()
        output_handler.print_success("Publisher created successfully.")
        logger.info("Publisher created successfully.")
    except Exception as e:
        db.connection.rollback()
        output_handler.print_error("An error occurred.")
        logger.error("An error occurred: %s", str(e))


def delete_publisher(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    publisher_name = input_handler.get_non_empty_input("Enter the name of the publisher to delete: ")
    query, params = verlag_query.create_delete_query(f"name = '{publisher_name}'")
    try:
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        db.connection.commit()
        output_handler.print_success("Publisher deleted successfully.")
        logger.info("Publisher deleted successfully.")
    except Exception as e:
        db.connection.rollback()
        output_handler.print_error("An error occurred.")
        logger.error("An error occurred: %s", str(e))


def create_menu_entry(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    data = input_handler.get_menu_data()
    query, params = menue_query.create_insert_query(data)
    try:
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        db.connection.commit()
        output_handler.print_success("Menu entry created successfully.")
        logger.info("Menu entry created successfully.")
    except Exception as e:
        db.connection.rollback()
        output_handler.print_error("An error occurred.")
        logger.error("An error occurred: %s", str(e))


def delete_menu_entry(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    menu_name = input_handler.get_non_empty_input("Enter the name of the menu entry to delete: ")
    query, params = menue_query.create_delete_query(f"name = '{menu_name}'")
    try:
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        db.connection.commit()
        output_handler.print_success("Menu entry deleted successfully.")
        logger.info("Menu entry deleted successfully.")
    except Exception as e:
        db.connection.rollback()
        output_handler.print_error("An error occurred.")
        logger.error("An error occurred: %s", str(e))


def create_reservation(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    data = input_handler.get_reservation_data()
    query, params = reservierung_query.create_insert_query(data)
    try:
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        db.connection.commit()
        output_handler.print_success("Reservation created successfully.")
        logger.info("Reservation created successfully.")
    except Exception as e:
        db.connection.rollback()
        output_handler.print_error("An error occurred.")
        logger.error("An error occurred: %s", str(e))


def delete_reservation(db, input_handler, output_handler, buch_query, autor_query, verlag_query, menue_query, reservierung_query):
    reservation_id = input_handler.get_integer_input("Enter the ID of the reservation to delete: ")
    query, params = reservierung_query.create_delete_query(f"id = {reservation_id}")
    try:
        cursor = db.connection.cursor()
        cursor.execute(query, params)
        db.connection.commit()
        output_handler.print_success("Reservation deleted successfully.")
        logger.info("Reservation deleted successfully.")
    except Exception as e:
        db.connection.rollback()
        output_handler.print_error("An error occurred.")
        logger.error("An error occurred: %s", str(e))


if __name__ == "__main__":
    main()
