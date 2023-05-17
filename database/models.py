from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON, Float, ForeignKey, DateTime)
from sqlalchemy import sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True, autoincrement=False, nullable=False)
    admin = Column(Boolean, default=False, nullable=False)
    balance = Column(Float, default=0, nullable=False)
    register_time = Column(DateTime, nullable=False)

    items = relationship("UserItem", back_populates="user")
    orders = relationship("Order", back_populates="user")


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String(250), nullable=True)
    show = Column(Boolean, default=True, nullable=False)
    title = Column(String(250), nullable=False)


class SubCategory(Base):
    __tablename__ = 'subcategory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String(250), nullable=True)
    show = Column(Boolean, default=True, nullable=False)
    title = Column(String(250), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"))


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    show = Column(Boolean, default=True, nullable=False)
    subcategory_id = Column(Integer, ForeignKey("subcategory.id", ondelete="CASCADE"))
    name = Column(String(250), nullable=False)
    photo = Column(String(250), nullable=True)
    price = Column(Integer, nullable=False)
    description = Column(String(255), nullable=True)

    files = relationship("ItemFiles", back_populates="item")


class ItemFiles(Base):
    __tablename__ = "item_files"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(String(150), nullable=False)

    item_id = Column(Integer, ForeignKey("items.id", ondelete="CASCADE"), nullable=False)
    item = relationship("Items", back_populates="files")


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)

    item_id = Column(Integer, ForeignKey("items.id", ondelete="CASCADE"))
    item = relationship("Item", back_populates="orders")

    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    user = relationship("Users", back_populates="orders")

    purchase_time = Column(DateTime)

    paid = Column(Boolean, default=False, nullable=False)
    summ = Column(Integer, nullable=True)
    quantity = Column(Integer, default=1, nullable=False)


class UsersItem(Base):
    __tablename__ = "users_item"

    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True
    )
    item_id = Column(
        Integer, ForeignKey("items.id", ondelete="CASCADE"), primary_key=True
    )
    quantity = Column(Integer, default=1, nullable=False)

    user = relationship("Users", back_populates="items")
    item = relationship("Item", back_populates="users")
