# models.py

class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns


class Buch(Table):
    def __init__(self):
        super().__init__("buch", ["id SERIAL PRIMARY KEY", "nummer INTEGER", "titel VARCHAR(100)"])


class Autor(Table):
    def __init__(self):
        super().__init__("autor", ["id SERIAL PRIMARY KEY", "name VARCHAR(100)", "kontakt VARCHAR(100)"])


class Verlag(Table):
    def __init__(self):
        super().__init__("verlag", ["id SERIAL PRIMARY KEY", "name VARCHAR(100)", "position VARCHAR(50)"])


class Reservierung(Table):
    def __init__(self):
        super().__init__("reservierung", ["id SERIAL PRIMARY KEY", "autor_id INTEGER", "buch_id INTEGER",
                                          "FOREIGN KEY(autor_id) REFERENCES autor(id)",
                                          "FOREIGN KEY(buch_id) REFERENCES buch(id)"])

class Menue(Table):
    def __init__(self):
        super().__init__("menue", ["id SERIAL PRIMARY KEY", "name VARCHAR(100)", "preis DECIMAL"])
