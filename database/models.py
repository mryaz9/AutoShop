from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON, Float, ForeignKey, DateTime)
from sqlalchemy import sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=False)
    admin = Column(Boolean, default=False)
    balance = Column(Float, default=0)
    register_time = Column(DateTime)


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String(250))
    show = Column(Boolean, default=True)
    title = Column(String(250))


class SubCategory(Base):
    __tablename__ = 'subcategory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String(250))
    show = Column(Boolean, default=True)
    title = Column(String(250))
    category_id = Column(Integer, ForeignKey("category.id"))


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    show = Column(Boolean, default=True)
    subcategory_id = Column(Integer, ForeignKey("subcategory.id"))
    name = Column(String(250))
    photo = Column(String(250))
    price = Column(Integer)
    description = Column(String(255))

    files = relationship("ItemFiles", back_populates="item")


class ItemFiles(Base):
    __tablename__ = "item_files"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(String(150), nullable=False)

    item_id = Column(Integer, ForeignKey("items.id"), nullable=False)
    item = relationship("Items", back_populates="files")


class Purchases(Base):
    __tablename__ = 'purchases'

    id = Column(Integer, primary_key=True, autoincrement=True)
    buyer_id = Column(Integer, ForeignKey("users.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    amount = Column(Integer)
    purchase_time = Column(DateTime)
    successful = Column(Boolean, default=False)

