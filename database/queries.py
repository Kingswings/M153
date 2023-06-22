# queries.py

from psycopg2 import sql


class Query:
    def __init__(self, table):
        self.table = table

    def insert(self, data):
        stmt = sql.SQL("INSERT INTO {} ({}) VALUES ({});").format(
            sql.Identifier(self.table.name),
            sql.SQL(', ').join(sql.Identifier(key) for key in data.keys()),
            sql.SQL(', ').join(sql.Placeholder() for _ in data.keys())
        )
        return stmt, list(data.values())

    def select_all(self):
        stmt = sql.SQL("SELECT * FROM {};").format(sql.Identifier(self.table.name))
        return stmt, []

    def update(self, condition, data):
        stmt = sql.SQL("UPDATE {} SET {} WHERE {};").format(
            sql.Identifier(self.table.name),
            sql.SQL(', ').join(sql.Identifier(key) + sql.SQL(' = ') + sql.Placeholder() for key in data.keys()),
            sql.SQL(condition)
        )
        return stmt, list(data.values())

    def delete(self, condition):
        stmt = sql.SQL("DELETE FROM {} WHERE {};").format(
            sql.Identifier(self.table.name),
            sql.SQL(condition)
        )
        return stmt, []

    def select_where(self, condition):
        stmt = sql.SQL("SELECT * FROM {} WHERE {};").format(
            sql.Identifier(self.table.name),
            sql.SQL(condition)
        )
        return stmt, []

    def search(self, column, value):
        query = sql.SQL("SELECT * FROM {} WHERE {} LIKE %s").format(self.table_name, sql.Identifier(column))
        params = (f"%{value}%",)
        return query, params
