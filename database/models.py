from sqlalchemy import (Column, Integer, BigInteger, String,
                        Boolean, Float, ForeignKey, DateTime, Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    photo = Column(String(250), nullable=True)
    subcategory = relationship("SubCategory", back_populates="category")


class SubCategory(Base):
    __tablename__ = 'subcategory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String(250), nullable=True)
    show = Column(Boolean, default=True, nullable=False)
    title = Column(String(250), nullable=False)
    category_id = Column(
        Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False
    )
    category = relationship("Category", back_populates="subcategory")
    items = relationship("Item", back_populates="subcategory")


class ItemFiles(Base):
    __tablename__ = "item_files"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(String(150), nullable=False)

    item_id = Column(
        Integer, ForeignKey("items.id", ondelete="CASCADE"), nullable=False
    )
    item = relationship("Item", back_populates="files")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    photo = Column(String(250), nullable=True)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, default=0, nullable=False)

    subcategory_id = Column(
        Integer, ForeignKey("subcategory.id", ondelete="CASCADE"), nullable=False
    )
    subcategory = relationship("SubCategory", back_populates="items")

    files = relationship("ItemFiles", back_populates="item")


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=False)

    admin = Column(Boolean, default=False, nullable=False)
    balance = Column(Float, default=0, nullable=False)
    register_time = Column(DateTime, nullable=False)


class MainMenu(Base):
    __tablename__ = "main_menu"

    id = Column(Integer, primary_key=True, autoincrement=True)

    main_menu = Column(String(250), default=None, nullable=True)
    catalog = Column(String(250), default=None, nullable=True)
    order = Column(String(250), default=None, nullable=True)
    profile = Column(String(250), default=None, nullable=True)
    info = Column(String(250), default=None, nullable=True)
    info_about = Column(String(250), default=None, nullable=True)

