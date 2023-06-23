from psycopg2 import sql

class Query:
    def __init__(self, table):
        self.table = table

    def create_insert_query(self, data):
        stmt = sql.SQL("INSERT INTO {} ({}) VALUES ({});").format(
            sql.Identifier(self.table.name),
            sql.SQL(', ').join(sql.Identifier(key) for key in data.keys()),
            sql.SQL(', ').join(sql.Placeholder() for _ in data.keys())
        )
        return stmt, list(data.values())

    def create_select_all_query(self):
        stmt = sql.SQL("SELECT * FROM {};").format(sql.Identifier(self.table.name))
        return stmt, []

    def create_update_query(self, condition, data):
        stmt = sql.SQL("UPDATE {} SET {} WHERE {};").format(
            sql.Identifier(self.table.name),
            sql.SQL(', ').join(sql.Identifier(key) + sql.SQL(' = ') + sql.Placeholder() for key in data.keys()),
            sql.SQL(condition)
        )
        return stmt, list(data.values())

    def create_delete_query(self, condition):
        stmt = sql.SQL("DELETE FROM {} WHERE {};").format(
            sql.Identifier(self.table.name),
            sql.SQL(condition)
        )
        return stmt, []

    def create_select_where_query(self, condition):
        stmt = sql.SQL("SELECT * FROM {} WHERE {};").format(
            sql.Identifier(self.table.name),
            sql.SQL(condition)
        )
        return stmt, []

    def create_search_query(self, table_name, column, value):
        query = sql.SQL("SELECT * FROM {} WHERE {} = %s").format(
            sql.Identifier(table_name), sql.Identifier(column)
        )
        params = (value,)
        return query, params
