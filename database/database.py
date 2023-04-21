import sqlite3
from itertools import chain


class DataBase:
    """Create DataBase"""

    def __init__(self, name_db: str, columns_db: list):
        self._name_db = name_db
        self._columns_db = columns_db

        self._connecting_db()
        self._creating_table_db()

    def __del__(self):
        self._connection.close()

    def _connecting_db(self):
        self._connection = sqlite3.connect(f"data_base_{self._name_db}.db")
        self._cursor = self._connection.cursor()

    def _creating_table_db(self):
        self._str_columns = " TEXT, ".join(self._columns_db)
        # TODO: Можно поменять _columns_db на словарь с ключами в виде типов переменных

        self._connection.execute(
            f'CREATE TABLE IF NOT EXISTS {self._name_db}(Id integer primary key autoincrement, {self._str_columns} TEXT)')
        self._connection.commit()

    def get_data_name(self, name: str):
        item = self._cursor.execute(f'SELECT * FROM {self._name_db} WHERE name == ?', (name, )).fetchall()
        return list(chain(*item))

    def del_data_name(self, name: str):
        self._cursor.execute('DELETE FROM shop WHERE name == ?', (name,))
        self._connection.commit()


class Users(DataBase):
    """DataBase for Users"""

    def __init__(self):
        super().__init__("User", ["user_id", "name", "card_name", "datetime_to_buy"])

    def set_data(self, data: list or dict or tuple):
        self._cursor.execute('INSERT INTO User VALUES (NULL, ?, ?, ?, ?)', data)
        self._connection.commit()


class Shop(DataBase):
    """DataBase for Shop"""

    def __init__(self):
        super().__init__("Shop", ["name", "price", "time_action", "discription"])

    def set_data(self, data: list or dict or tuple):
        self._cursor.execute('INSERT INTO User VALUES (NULL, ?, ?, ?, ?)', data)
        self._connection.commit()