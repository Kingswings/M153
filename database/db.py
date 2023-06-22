# db.py
import psycopg2


class Database:
    def __init__(self, config):
        self.config = config
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = psycopg2.connect(dbname=self.config["dbname"], user=self.config["user"],
                                               password=self.config["password"], host=self.config["host"])
        return self.connection

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS buch (
                id SERIAL PRIMARY KEY,
                nummer INT NOT NULL UNIQUE,
                titel VARCHAR(100)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS autor (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                kontakt VARCHAR(255)
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS verlag (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                stellung VARCHAR(255),
                gehalt DECIMAL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reservierung (
                id SERIAL PRIMARY KEY,
                autor_id INT REFERENCES autor(id),
                buch_id INT REFERENCES buch(id),
                datum DATE NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS menue (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                preis DECIMAL NOT NULL
            );
        """)
        self.connection.commit()

    def disconnect(self):
        if self.connection:
            self.connection.close()
