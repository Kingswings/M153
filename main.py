from cli.input import UserInputHandler
from cli.output import UserOutputHandler
from config import DB_CONFIG
from database.db import Database
from database.models import Autor, Buch, Verlag, Menue, Reservierung
from database.queries import Query
from logger import logger


def main():
    # Erstellen Sie Instanzen der Klassen
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

    # Hauptmenü
    while True:
        choice = input_handler.get_menu_choice()

        if choice == 1:  # Buch anlegen
            data = input_handler.get_book_data()
            query, params = buch_query.insert(data)
            try:
                cursor = db.connection.cursor()
                cursor.execute(query, params)
                db.connection.commit()
                output_handler.print_success("Buch erfolgreich angelegt.")
                logger.info("Buch erfolgreich angelegt.")
            except Exception as e:
                db.connection.rollback()
                if "unique constraint" in str(e).lower():
                    output_handler.print_error("Ein Buch mit dieser Nummer existiert bereits.")
                    logger.error("Ein Buch mit dieser Nummer existiert bereits.")
                else:
                    output_handler.print_error("Ein Fehler ist aufgetreten.")
                    logger.error("Ein Fehler ist aufgetreten: %s", str(e))
                    
        elif choice == 2:  # Buch löschen
            buch_nummer = input_handler.get_integer_input("Geben Sie die Nummer des zu löschenden Buches ein: ")
            query, params = buch_query.delete(f"nummer = {buch_nummer}")
            try:
                cursor = db.connection.cursor()
                cursor.execute(query, params)
                db.connection.commit()
                if cursor.rowcount == 0:
                    raise Exception("Buch existiert nicht.")
                output_handler.print_success("Buch erfolgreich gelöscht.")
                logger.info("Buch erfolgreich gelöscht.")
            except Exception as e:
                db.connection.rollback()  # Rollback der Transaktion, um den Fehlerzustand zu löschen
                if "Buch existiert nicht" in str(e):
                    output_handler.print_error("Es gibt keinen Buch mit dieser Nummer.")
                    logger.error("Es gibt keinen Buch mit dieser Nummer.")
                else:
                    output_handler.print_error("Ein Fehler ist aufgetreten.")
                    logger.error("Ein Fehler ist aufgetreten: %s", str(e))
                    
        elif choice == 3:  # Buch bearbeiten
            try:
                data = input_handler.get_book_data()  # Get the updated book data
                condition = "nummer = {}".format(data['nummer'])  # Assuming 'nummer' is the primary key or unique identifier
                stmt, values = buch_query.update(condition, data)
                cursor = db.connection.cursor()
                cursor.execute(stmt, values)
                db.connection.commit()
                output_handler.print_success("Buch wurde erfolgreich bearbeitet")
                logger.info("Buch wurde bearbeitet")
            except Exception as e:
                db.connection.rollback()
                output_handler.print_error("Ein Fehler ist aufgetreten.")
                logger.error("Ein Fehler ist aufgetreten: %s", str(e))

        elif choice == 4: # buch suchen
            data = input_handler.get_book_data()
            condition = "nummer = {}".format(data['nummer'])
            query, params = buch_query.select_where(condition)
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
                output_handler.print_error("Ein Fehler ist aufgetreten.")
                logger.error("Ein Fehler ist aufgetreten: %s", str(e))

        elif choice == 5:  # Buch suchen
            table_name = "buch"  # Replace with the appropriate table name
            column = input_handler.get_non_empty_input("Geben Sie den Spaltennamen ein: ")
            value = input_handler.get_non_empty_input("Geben Sie den Suchwert ein: ")
            query, params = buch_query.search(table_name, column, value)
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
                output_handler.print_error("Ein Fehler ist aufgetreten.")
                logger.error("Ein Fehler ist aufgetreten: %s", str(e))

        elif choice == 6:  # Autor anlegen
            data = input_handler.get_autor_data()
            query, params = autor_query.insert(data)
            try:
                cursor = db.connection.cursor()
                cursor.execute(query, params)
                db.connection.commit()
                output_handler.print_success("Autor erfolgreich angelegt.")
                logger.info("Autor erfolgreich angelegt.")
            except Exception as e:
                db.connection.rollback()
                output_handler.print_error("Ein Fehler ist aufgetreten.")
                logger.error("Ein Fehler ist aufgetreten: %s", str(e))

        elif choice == 7:  # Autor löschen
            autor_name = input_handler.get_non_empty_input("Geben Sie den Namen des zu löschenden Autors ein: ")
            query, params = autor_query.delete(f"name = '{autor_name}'")
            try:
                cursor = db.connection.cursor()
                cursor.execute(query, params)
                db.connection.commit()
                output_handler.print_success("Autor erfolgreich gelöscht.")
                logger.info("Autor erfolgreich gelöscht.")
            except Exception as e:
                db.connection.rollback()
                output_handler.print_error("Ein Fehler ist aufgetreten.")
                logger.error("Ein Fehler ist aufgetreten: %s", str(e))
        
        elif choice == 8:  # Verlag anlegen
            data = input_handler.get_distributioner_data()
            query, params = verlag_query.insert(data)
            try:
                cursor = db.connection.cursor()
                cursor.execute(query, params)
                db.connection.commit()
                output_handler.print_success("Verlag erfolgreich angelegt.")
                logger.info("Verlag erfolgreich angelegt.")
            except Exception as e:
                db.connection.rollback()
                output_handler.print_error("Ein Fehler ist aufgetreten.")
                logger.error("Ein Fehler ist aufgetreten: %s", str(e))

        elif choice == 9:  # Verlag löschen
            verlag_name = input_handler.get_non_empty_input("Geben Sie den Namen des zu löschenden Verlags ein: ")
            query, params = verlag_query.delete(f"name = '{verlag_name}'")
            try:
                cursor = db.connection.cursor()
                cursor.execute(query, params)
                db.connection.commit()
                output_handler.print_success("Verlag erfolgreich gelöscht.")
                logger.info("Verlag erfolgreich gelöscht.")
            except Exception as e:
                db.connection.rollback()
                output_handler.print_error("Ein Fehler ist aufgetreten.")
                logger.error("Ein Fehler ist aufgetreten: %s", str(e))

        elif choice == 10:  # Menüeintrag anlegen
            data = input_handler.get_menu_data()
            query, params = menue_query.insert(data)
            try:
                cursor = db.connection.cursor()
                cursor.execute(query, params)
                db.connection.commit()
                output_handler.print_success("Menüeintrag erfolgreich angelegt.")
                logger.info("Menüeintrag erfolgreich angelegt.")
            except Exception as e:
                db.connection.rollback()
                output_handler.print_error("Ein Fehler ist aufgetreten.")
                logger.error("Ein Fehler ist aufgetreten: %s", str(e))

        elif choice == 11:  # Menüeintrag löschen
            menu_name = input_handler.get_non_empty_input("Geben Sie den Namen des zu löschenden Menüeintrags ein: ")
            query, params = menue_query.delete(f"name = '{menu_name}'")
            try:
                cursor = db.connection.cursor()
                cursor.execute(query, params)
                db.connection.commit()
                output_handler.print_success("Menüeintrag erfolgreich gelöscht.")
                logger.info("Menüeintrag erfolgreich gelöscht.")
            except Exception as e:
                db.connection.rollback()
                output_handler.print_error("Ein Fehler ist aufgetreten.")
                logger.error("Ein Fehler ist aufgetreten: %s", str(e))

        elif choice == 12:  # Reservierung anlegen
            data = input_handler.get_reservation_data()
            query, params = reservierung_query.insert(data)
            try:
                cursor = db.connection.cursor()
                cursor.execute(query, params)
                db.connection.commit()
                output_handler.print_success("Reservierung erfolgreich angelegt.")
                logger.info("Reservierung erfolgreich angelegt.")
            except Exception as e:
                db.connection.rollback()
                output_handler.print_error("Ein Fehler ist aufgetreten.")
                logger.error("Ein Fehler ist aufgetreten: %s", str(e))
        
        elif choice == 13:  # Reservierung löschen
            reservierung_id = input_handler.get_integer_input("Geben Sie die ID der zu löschenden Reservierung ein: ")
            query, params = reservierung_query.delete(f"id = {reservierung_id}")
            try:
                cursor = db.connection.cursor()
                cursor.execute(query, params)
                db.connection.commit()
                if cursor.rowcount == 0:
                    raise Exception("Reservierung existiert nicht.")
                output_handler.print_success("Reservierung erfolgreich gelöscht.")
                logger.info("Reservierung erfolgreich gelöscht.")
            except Exception as e:
                db.connection.rollback()  # Rollback der Transaktion, um den Fehlerzustand zu löschen
                if "Reservierung existiert nicht" in str(e):
                    output_handler.print_error("Es gibt keine Reservierung mit dieser ID.")
                    logger.error("Es gibt keine Reservierung mit dieser ID.")
                else:
                    output_handler.print_error("Ein Fehler ist aufgetreten.")
                    logger.error("Ein Fehler ist aufgetreten: %s", str(e))
                    
        else:
            output_handler.print_error("Ungültige Auswahl, bitte versuchen Sie es erneut.")
            logger.warning("Ungültige Auswahl, bitte versuchen Sie es erneut.")


if __name__ == "__main__":
    main()
