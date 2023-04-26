import sqlite3
from itertools import chain
from dataclasses import astuple, asdict

from .Models import AdminData, ColumnsData, ShopData


class DataBase:
    """Create DataBase"""

    def __init__(self, name_db: str, columns_db: list):
        self._name_db = name_db
        self._columns_db = columns_db

        self._connecting_db()
        self._creating_table_db()

    def _connecting_db(self):
        self._connection = sqlite3.connect(f"data_base_{self._name_db}.db")
        self._cursor = self._connection.cursor()

    def _creating_table_db(self):
        self._str_columns = " TEXT, ".join(self._columns_db)
        # TODO: Можно поменять _columns_db на словарь с ключами в виде типов переменных

        self._connection.execute(
            f'CREATE TABLE IF NOT EXISTS {self._name_db}(Id integer primary key autoincrement, {self._str_columns} TEXT)')
        self._connection.commit()

    def get_full_data(self):
        item = self._cursor.execute(f'SELECT * FROM {self._name_db}').fetchall()
        return list(chain(*item))

    def get_data_user_id(self, user_id: int):
        item = self._cursor.execute(f'SELECT * FROM {self._name_db} WHERE user_id == ?', (user_id,)).fetchall()
        return list(chain(*item))

    def del_data_name(self, name: str):
        self._cursor.execute('DELETE FROM shop WHERE name == ?', (name,))
        self._connection.commit()

    #def __del__(self): # TODO: self._connection.close() AttributeError: 'Users' object has no attribute '_connection'
    #    self._connection.close()


class Users(DataBase):
    """DataBase for Users"""

    def __init__(self):
        super().__init__(name_db="User", columns_db=list(asdict(ColumnsData()).keys())) #Иничиализирует датакласс и вытягивает ключи

    def set_data(self, data: ColumnsData):
        self._cursor.execute('INSERT INTO User VALUES (NULL, ?, ?, ?, ?, ?)', astuple(data))
        self._connection.commit()


class Admin(DataBase):
    def __init__(self):
        super().__init__(name_db="Admins", columns_db=list(asdict(AdminData()).keys()))

    def set_data(self, data: AdminData):
        self._cursor.execute('INSERT INTO Admins VALUES (NULL, ?, ?)', astuple(data))
        self._connection.commit()


class Shop(DataBase):
    """DataBase for Shop"""
    def __init__(self):
        super().__init__(name_db="Shop", columns_db=list(asdict(ShopData()).keys()))

    def set_data(self, data: ShopData):
        self._cursor.execute('INSERT INTO Shop VALUES (NULL, ?, ?, ?, ?, ?)', astuple(data))
        self._connection.commit()

    def get_data_catalog(self, catalog: str):
        list_item = []
        item = self._cursor.execute(f'SELECT * FROM {self._name_db} WHERE catalog == ?', (catalog,)).fetchall()
        for ret in item:
            list_item.append(ret)
        return list_item
        #return list(chain(*item))


from aiogram import types, Bot
from gino import Gino
from gino.schema import GinoSchemaVisitor


from config import db_pass, db_user, host

db = Gino()


# Документация
# http://gino.fantix.pro/en/latest/tutorials/tutorial.html




class DBCommands:

    async def get_user(self, user_id):
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    async def add_new_user(self, referral=None):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.username = user.username
        new_user.full_name = user.full_name

        if referral:
            new_user.referral = int(referral)
        await new_user.create()
        return new_user

    async def set_language(self, language):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(language=language).apply()

    async def count_users(self) -> int:
        total = await db.func.count(User.id).gino.scalar()
        return total

    async def check_referrals(self):
        bot = Bot.get_current()
        user_id = types.User.get_current().id

        user = await User.query.where(User.user_id == user_id).gino.first()
        referrals = await User.query.where(User.referral == user.id).gino.all()

        return ", ".join([
            f"{num + 1}. " + (await bot.get_chat(referral.user_id)).get_mention(as_html=True)
            for num, referral in enumerate(referrals)
        ])

    async def show_items(self):
        items = await Item.query.gino.all()

        return items


async def create_db():
    await db.set_bind(f'postgresql://{db_user}:{db_pass}@{host}/gino')

    # Create tables
    db.gino: GinoSchemaVisitor
    #await db.gino.drop_all()
    await db.gino.create_all()