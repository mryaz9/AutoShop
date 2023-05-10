from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON, Float, ForeignKey, DateTime)
from sqlalchemy import sql
from sqlalchemy.orm import relationship

from database.init_database import db


class Users(db.Model):
    __tablename__ = 'users'
    query: sql.Select

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    full_name = Column(String(100))
    username = Column(String(50))
    balance = Column(Float, default=0)

    def __repr__(self):
        return "<Users(id='{}', fullname='{}', username='{}', balance='{}')>".format(
            self.id, self.full_name, self.username, self.balance)


class Admins(db.Model):
    __tablename__ = 'admins'
    query: sql.Select

    id = Column(Integer, Sequence('admin_id_seq'), primary_key=True)
    user_id = Column(BigInteger, primary_key=True)

    def __repr__(self):
        return "<Admins(id='{}', user_id='{}')>".format(
            self.id, self.user_id)


class Category(db.Model):
    __tablename__ = 'category'
    query: sql.Select

    id = Column(Integer, Sequence('category_id_seq'), primary_key=True)
    category_name = Column(String(250))


class SubCategory(db.Model):
    __tablename__ = 'subcategory'
    query: sql.Select

    id = Column(Integer, Sequence('subcategory_id_seq'), primary_key=True)
    subcategory_name = Column(String(250))
    category_id = Column(Integer, ForeignKey("category.id"))


class Items(db.Model):
    __tablename__ = 'items'
    query: sql.Select

    id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    show = Column(Boolean, default=True)

    subcategory_id = Column(Integer, ForeignKey("subcategory.id"))

    name = Column(String(50))
    amount = Column(Integer)
    # files = Column(JSON)
    photo = Column(String(250))
    price = Column(Integer)
    time_action = Column(Integer)
    description = Column(String(255))

    admin_id_add = Column(Integer)

    def __repr__(self):
        return "<Items(id='{}', show='{}', subcategory_id='{}', name='{}', price='{}')>".format(
            self.id, self.show, self.subcategory_id, self.name, self.price)


class Purchases(db.Model):
    __tablename__ = 'purchases'
    query: sql.Select

    id = Column(Integer, Sequence('purchases_id_seq'), primary_key=True)
    buyer_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    amount = Column(Integer)
    purchase_time = Column(DateTime)
    successful = Column(Boolean, default=False)

    def __repr__(self):
        return "<Purchases(id='{}', buyer='{}', item_id='{}', purchase_time='{}', successful='{}')>".format(
            self.id, self.buyer, self.item_id, self.purchase_time, self.successful)
