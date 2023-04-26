from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON, Float)
from sqlalchemy import sql

from database.init_database import db


class Users(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    full_name = Column(String(100))
    username = Column(String(50))
    balance = Column(Float, default=0)

    query: sql.Select

    def __repr__(self):
        return "<Users(id='{}', fullname='{}', username='{}', balance='{}')>".format(
            self.id, self.full_name, self.username, self.balance)


class Admins(db.Model):
    __tablename__ = 'admins'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)

    def __repr__(self):
        return "<Admins(id='{}', user_id='{}')>".format(
            self.id, self.user_id)


class Items(db.Model):
    __tablename__ = 'items'
    query: sql.Select

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    show = Column(Boolean, default=False)
    category_code = Column(String(20))
    category_name = Column(String(50))
    subcategory_code = Column(String(50))
    subcategory_name = Column(String(20))

    name = Column(String(50))
    photo = Column(String(250))
    price = Column(Integer)
    time_action = Column(TIMESTAMP)
    fill_description = Column(String(255))

    admin_id_add = Column(BigInteger)

    def __repr__(self):
        return "<Items(id='{}', show='{}', category_code='{}', subcategory_code='{}', name='{}', price='{}')>".format(
            self.id, self.show, self.category_code, self.subcategory_code, self.name, self.price)


class Purchases(db.Model):
    __tablename__ = 'purchases'
    query: sql.Select

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    buyer_id = Column(BigInteger)
    item_id = Column(BigInteger)
    purchase_time = Column(TIMESTAMP)
    successful = Column(Boolean, default=False)

    def __repr__(self):
        return "<Purchases(id='{}', buyer='{}', item_id='{}', purchase_time='{}', successful='{}')>".format(
            self.id, self.buyer, self.item_id, self.purchase_time, self.successful)
